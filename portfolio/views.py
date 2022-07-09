from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def home(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'home.html',context)
def detail(request,id):
    post = get_object_or_404(Post, pk=id)
    return render(request,'detail.html',{"post":post})