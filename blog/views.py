from django.shortcuts import render
from .models import Post, Project, AboutMe

def home(request):
    return render(request, 'blog/home.html')

def resume_page(request):
    return render(request, 'blog/resume.html')
