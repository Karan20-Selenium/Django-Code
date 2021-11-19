from django.contrib import admin
from .models import Post, User1

# Register your models here.

@admin.register(User1)
class User1Admin(admin.ModelAdmin):
    list_display = ['username','password']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['post_title', 'post_cat', 'post_publish_date','user']


