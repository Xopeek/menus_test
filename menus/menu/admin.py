from django.contrib import admin

from menu.models import MenuCategory, Menu


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'long_name']
    list_display = ['__str__',]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'link', 'parent_item']
    list_display = ['__str__', 'category', 'link', 'parent_item']
