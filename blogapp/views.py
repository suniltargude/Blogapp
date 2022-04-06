from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from blogapp.models import Posts
from blogapp.forms import CreateBlogForm , UpdateBlogForm
from django.contrib.auth.decorators import login_required

def register_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")

    return render(request , "blogapp/user_register.html" , {"form" : form})

@login_required
def posts_list_view(request):
    posts= Posts.objects.all()
    return render(request , "blogapp/list.html" , {'posts': posts})

@login_required
def create_new_blog_view(request):
    form = CreateBlogForm()

    if request.method == 'POST':
        form = CreateBlogForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/list/")

    return render(request , "blogapp/create_blog.html" , {"form" : form})


@login_required
def detail_blog_view(request , id):
    obj = Posts.objects.get(pk = id)
    return render(request , "blogapp/detail_blog.html" , {"obj" : obj})

@login_required
def update_view(request , id):
    obj = Posts.objects.get(pk = id)
    form = UpdateBlogForm(instance=obj)

    if request.method == 'POST':
        form = UpdateBlogForm(request.POST, request.FILES, instance=obj)
        if form .is_valid():
            form.save()
            return redirect(f'/detail/blog/{obj.id}/')

    return render(request , "blogapp/update.html" , {"obj" : obj , 'form':form})


@login_required
def delete_view(request , id):
    obj = Posts.objects.get(pk = id)
    obj.delete()
    return redirect('/list/')

 