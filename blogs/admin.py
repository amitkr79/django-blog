from django.contrib import admin
from .models import Category,Blog,AuthorProfile,SocialLink

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ('user','joined')
    inlines = [SocialLinkInline]

#prepopulating hte slug field as per the title
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','author','status','is_featured','created_at')
    search_fields =('id','title','category__category_name','status','author__username')
    list_editable= ('is_featured',)
    
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(AuthorProfile,AuthorProfileAdmin)
