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

class CategoryView(TemplateView):
    template_name = 'category.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class DetailsView(TemplateView):
    template_name = 'post-details.html'

class PrivacyView(TemplateView):
    template_name = 'privacy.html'

class Index2View(TemplateView):
    template_name = 'index-2.html'

class Index3View(TemplateView):
    template_name = 'index-3.html'

class About2View(TemplateView):
    template_name = 'about-2.html'

class Contact2View(TemplateView):
    template_name = 'contact-2.html'