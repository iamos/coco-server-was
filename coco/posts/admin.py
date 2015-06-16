from django.contrib import admin
from posts.models import Post
from posts.models import Photo
from posts.models import Tag
from posts.models import Comment

class PostAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'tags']
    ordering = ['-created_at']
    

class TagAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']
    list_editable = ['name']
    search_fields = ['name']
    ordering = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(Photo)
