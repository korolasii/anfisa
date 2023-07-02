from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'content']
    list_display = ['name', 'content', 'created_at']
    list_filter = ['name', 'content', 'created_at']
    
admin.site.register(Comment, CommentAdmin)