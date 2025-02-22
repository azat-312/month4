from django.shortcuts import render,HttpResponse, redirect
from posts.models import Post

from posts.forms import PostCreateForm , SearchForm

from django.contrib.auth.decorators import login_required
from django.db.models import Q



def test_view(request):
    return HttpResponse (f"ну что-то крутое")

def html_view(request):
    return render(request, "main.html")

@login_required(login_url="/login/")
def post_list_view(request):
    form = SearchForm()
    query_params = request.GET
    limit = 3
    posts = Post.objects.all()
    search = query_params.get("search")
    category_id = query_params.get("category")
    tags = query_params.getlist("tags")
    ordering = query_params.get("ordering")
    page = int(query_params.get("page"))if query_params.get("page") else 1
    if search:
        posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
    if category_id:
        posts = posts.filter(category_id=category_id)
    if tags:
        tags =[int (tag)for tag in tags]
        posts = posts.filter(tags__id__in=tags)
    if ordering:
        posts = posts.order_by(ordering)
    max_pages = posts.count() / limit
    if round(max_pages) < max_pages:
        max_pages = round(max_pages) + 1
    else:
        max_pages = round(max_pages)

    start = (page -1) * limit
    end = page * limit
    posts = posts[start:end]
    context_data={"posts": posts,"form":form, "max_pages": range(1, max_pages+1)}
    return render(
        request, "posts/post_list.html",context=context_data
    )

@login_required(login_url="/login/")    
def post_detail_view(request,post_id):
    post = Post.objects.get(id=post_id)
    return render (request, "posts/post_detail.html", context={"post":post})


@login_required(login_url="/login/")
def create_post_view(request):
    form = PostCreateForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect("/posts/")
    else:
        return render(request,'posts/create_post.html',{'form':form})