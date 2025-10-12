from django.shortcuts import render,redirect, HttpResponse
from . models import Messages
from django.contrib import messages
from blog.models import Post

# Create your views here.
def home(request):
    return render(request,'home/home.html') 

def about(request):
    return render(request,'home/about.html') 

# def contact(request):
#     messages.success(request, 'Welcome to the page')
#     if request.method == 'POST':
#         name = request.POST['name']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         content = request.POST['content']
#         contact = Contact(name=name, email=email, phone=phone, content=content)
#         contact.save()
#         print(name, phone, email, content)
#     return render(request,'home/contact.html') 

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        content = request.POST.get('content')

        if len(name) < 2 or len(phone) < 10 or len(email) < 3 or len(content) < 4:
            messages.error(request, "Please fill the form correctly.")
        else:
            Messages.objects.create(name=name, email=email, phone=phone, content=content)
            messages.success(request, "Your message has been delivered.")
            return redirect('contact') 

    return render(request, 'home/contact.html')


def search(request):
    query = request.GET.get('query', '')
    if query:
        allPosts = Post.objects.filter(title__icontains=query)
    else:
        allPosts = Post.objects.none()
    context = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', context)

