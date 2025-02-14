from django.shortcuts import render,HttpResponse
from posts.models import Post
from .forms import PostCreateForm
from django.shortcuts import redirect


def test_view(request):
    return HttpResponse (f"ну что-то крутое")

def html_view(request):
    return render(request, "main.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})
    
def post_detail_view(request,post_id):
    post = Post.objects.get(id=post_id)
    return render (request, "posts/post_detail.html", context={"post":post})


def create_post_view(request):
    form = PostCreateForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect("/posts/")
    else:
        return render(request,'posts/create_post.html',{'form':form})