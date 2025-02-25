from django.shortcuts import render,HttpResponse, redirect
from posts.models import Post
from django.views import View
from posts.forms import PostCreateForm , SearchForm , PostUpdateForm
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q


class TestView(View):
    def get(self,request):
        return HttpResponse (f"ну что-то крутое")

def html_view(request):
    return render(request, "main.html")

class PostListView(ListView):
    model=Post
    template_name="posts/post_list.html"
    paginate_by = 3
    context_object_name = "posts"

class PostDetailView(DetailView):
    model=Post
    template_name= "posts/post_detail.html"
    context_object_name = "post"
    pk_url_kwarg="post_id"

class PostCreateView(CreateView):
    model = Post
    success_url = "posts/class"
    form_class =PostUpdateForm
    template_name = "posts/post_create.html"



@login_required(login_url="/login/")
def update_post_view(request,post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponse ("no post")
    if request.method == "GET":
        form= PostUpdateForm(instance=post)
        return render(request, "posts/update_post.html",context={"form":form})
    if request.method == "POST":
        form = PostUpdateForm(request.POST,request.FILES, instance=post)
        if not form.is_valid():
            return render(request, "posts/update_post.html",context={"form":form})
        elif form.is_valid():
            form.save()
            return redirect("/profile/")
        else:
            return HttpResponse ("fuck is not work try again")