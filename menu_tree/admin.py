from django.contrib import admin
from .models import Menu, Submenu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'uri']

class SubmenuAdmin(admin.ModelAdmin):
    list_display = ['submenu_name', 'menu', 'parent_menu', 'uri', 'named_url']
    list_editable = ['menu', 'parent_menu', 'uri', 'named_url']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Submenu, SubmenuAdmin)
