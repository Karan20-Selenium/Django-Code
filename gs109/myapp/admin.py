from django.contrib import admin
from .models import Page
from .models import Book


# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
 list_display=['page_name', 'page_cat', 'page_publish_date', 'user']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
 list_display = ['book_name','subject','panna']
