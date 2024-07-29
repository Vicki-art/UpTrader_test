from django import template
from menu_tree.models import Submenu
from django.urls import reverse

register = template.Library()


@register.inclusion_tag('menu_tree/tree_template.html', takes_context=True)
def draw_menu(context, requested_menu):
    current_url = context['request'].build_absolute_uri()

    # Make extract from the DB and filter DB instances by requested menu
    extract = Submenu.objects.select_related('parent_menu', 'menu').all()
    all_menus = []
    for item in extract:
        if item.menu.name == requested_menu:
            all_menus.append(item)

    # Convert database sample to convenient data structure which provides nesting levels for recursive rendering
    tree_dict = {}
    menu_dict = []
    # current_item = None

    for item in all_menus:
        tree_dict[item.id] = {}
        tree_dict[item.id]['id'] = item.id
        tree_dict[item.id]['menu'] = requested_menu
        tree_dict[item.id]['title'] = item.submenu_name
        tree_dict[item.id]['children'] = []
        if item.parent_menu:
            tree_dict[item.id]['parent'] = item.parent_menu

    # Defining url through direct url or named url
        if item.named_url:
            tree_dict[item.id]['url'] = reverse(item.named_url)
        else:
            tree_dict[item.id]['url'] = reverse('demo', args=(item.uri,))

    # Defining current item to organise drop-down points
        if current_url.endswith(tree_dict[item.id]['url']):
            tree_dict[item.id]['open'] = True
            tree_dict[item.id]['current'] = True
            if item.parent_menu:
                tree_dict[item.parent_menu.id]['open'] = True
        else:
            tree_dict[item.id]['open'] = False

    # Defining the order and nesting
    for item in tree_dict:
        parent = tree_dict[item].get('parent', None)
        if parent:
            tree_dict[parent.id]['children'].append(tree_dict[item])
        else:
            menu_dict.append(tree_dict[item])

    return {'menu_name': requested_menu, 'menus': menu_dict}

#Additional custom tag for drawing submenus
@register.inclusion_tag('menu_tree/tree_leaves.html')
def draw_leave(leaves: list):
    return {'leaves': leaves}
