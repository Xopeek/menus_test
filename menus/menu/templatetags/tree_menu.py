import re

from django import template
from django.http import HttpRequest
from django.urls import reverse, NoReverseMatch

from menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_custom_menu(context, menu_name='', parent_id=0):
    is_url = re.compile(r'^http[s]?://')
    if 'request' in context and isinstance(context['request'], HttpRequest):
        current_path = context['request'].path
    else:
        current_path = ''

    menu_items = Menu.objects.select_related('category').filter(
        category__name=menu_name
    ).order_by('pk')
    menu = []

    for item in menu_items:
        path = item.link.strip()
        target = '_self'
        if is_url.match(path):
            url = path
            target = '_blank'
        else:
            try:
                url = reverse(path)
            except NoReverseMatch:
                url = path

        menu.append({
            'id': item.pk,
            'url': url,
            'target': target,
            'name': item.name,
            'parent_id': item.parent_item or 0,
            'active': url == current_path,
        })

    current_menu = [item for item in menu if item['parent_id'] == parent_id]

    return {
        'menu': menu,
        'current_menu': current_menu,
    }
