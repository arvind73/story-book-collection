from django.contrib import admin
from .models import Story, Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']

@admin.register(Story)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','publish_date']
