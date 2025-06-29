from django.shortcuts import render
from .models import Post, Project, AboutMe

def home(request):
    posts = Post.objects.order_by('-created_at')[:5]  # آخرین 5 پست
    projects = Project.objects.order_by('-created_at')[:5]
    about = AboutMe.objects.first()
    return render(request, 'blog/home.html', {'posts': posts, 'projects': projects, 'about': about})

def resume_page(request):
    return render(request, 'blog/resume.html')
