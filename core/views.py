from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView

def home(request):
    posts = Post.objects.all()
    topposts = TopPost.objects.all()
    admins = Admin.objects.all()
    content = {
        "posts": posts,
        "topposts": topposts,
        "admins": admins
    }
    return render(request, 'index.html', content)

class AboutView(TemplateView):
    template_name = 'about.html'