from django.shortcuts import render
from .models import MenuItem


def draw_menu(request, menu_name):
    try:
        menu = MenuItem.objects.get(name=menu_name)
    except MenuItem.DoesNotExist:
        return render(request, 'menu_not_found.html')
