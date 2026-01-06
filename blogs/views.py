from django.shortcuts import render
from  .models import Blog,Category
from django.shortcuts import get_object_or_404,redirect
from django.db.models import Q
# Create your views here.

def posts_by_category(request,category_id):
    # fetch the post that belongs to the category with the id
    posts = Blog.objects.filter(status='Published',category = category_id)
    
    # Use try/except when we want to achieve some action manually controll the user navigation
    
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    
    # use below when you want to show the 404 page `    if not found
    category = get_object_or_404(Category,pk=category_id)
    context = {
        'posts':posts,
        'category':category
    }
    return render(request,'posts_by_category.html',context)
    
    
def blogs(request,slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        "single_blog":single_blog
    }
    return render(request, 'blogs.html', context)
    
def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        "blogs":blogs,
        "keyword":keyword,
    }
    return render(request,'search.html',context)