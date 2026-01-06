from django.shortcuts import render
from  .models import Blog,Category
from django.shortcuts import get_object_or_404,redirect
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
    