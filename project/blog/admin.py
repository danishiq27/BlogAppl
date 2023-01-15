from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.
class CommentItemsInLine(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields=['title', 'intro', 'body']
    list_display=['title', 'slug', 'category','created','status']
    list_filter = ['category', 'created','status']
    inlines = [CommentItemsInLine]
    prepopulated_fields = {'slug': ('title',)} 

class CategoryAdmin(admin.ModelAdmin):
    search_fields=['title'] 
    list_display=['title']
    prepopulated_fields = {'slug': ('title',)}

class CommentsAdmin(admin.ModelAdmin):
    search_fields=['name', 'post', 'created'] 
       

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentsAdmin)
