from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog,AuthorProfile

def home(request):
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status='Published')

    profile = AuthorProfile.objects.first()

    context={
        'featured_posts':featured_posts,
        'posts':posts,
        'profile':profile
    }
    return render(request,'home.html',context)