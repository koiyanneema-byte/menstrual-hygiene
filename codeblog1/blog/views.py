from django.shortcuts import render, HttpResponse
from django.contrib import messages
from . models import Post
from datetime import datetime


# Create your views here.
def blog(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'blog/blog.html', context) 

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request,'blog/blogpost.html', context) 

def search(request):
    return HttpResponse('This is search')



def addBlog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        slug = request.POST.get('slug')
        content = request.POST.get('content')
        timestamp = request.POST.get('timestamp')
        image = request.FILES.get('image')

        # Basic validation
        if len(title) < 3 or len(author) < 2 or len(slug) < 3 or len(content) < 10:
            messages.error(request, "Please fill the form correctly.")
        else:
            post = Post(
                title=title,
                author=author,
                slug=slug,
                content=content,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%dT%H:%M") if timestamp else datetime.now(),
                image=image
            )
            post.save()
            messages.success(request, "Your blog has been posted successfully!")
            print(title, author, slug, content, timestamp, image)

    return render(request, 'blog/addblog.html')
