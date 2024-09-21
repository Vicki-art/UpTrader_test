The Task:
To make a django app that will implement a tree menu. 
It should allow you to enter a menu (one or more) into the database via the admin panel, and draw a menu by name on any desired page
with {% draw_mnenu 'main_menu' %}

Conditions:
1) The menu is implemented via a template tag;
2) Everything above the selected item is expanded. The first level of nesting under the selected item is also expanded;
3) Stored in the database;
4) Edited in the standard Django admin panel;
5) The active menu item is determined based on the URL of the current page;
6) There can be several menus on one page. They are determined by name;
7) When you click on a menu, you go to the URL specified in it. The URL can be specified either explicitly or via a named URL;
8) Each menu requires exactly 1 query to the database;
9) only Django and the standard Python library should be used when performing the task;

Setting up the current app:
To run my application you will need:
1) To copy the repository: https://github.com/Vicki-art/UpTrader_test.git;
2) To install Django (4.2.3) and Python (ver=3.11);
3) To apply migrations (python3 manage.py migrate);
4) To run the server (python3 manage.py runserver).
   
Usage tips:
1) You can create your menu through Django admin panel (link: http://127.0.0.1:8000/admin/menu_tree/menu/, where http://localhost:8000 - is your app address).
Here you can create your menu by setting the name and uri.
2) Submenus can also be created in Django admin panel (link: http://127.0.0.1:8000/admin/menu_tree/submenu/).
3) To display the menu, you need to load the template tag:
{% load menu_tags %} and then call this tag in the required place in html template {% draw_menu 'requested_menu' %}

* requested_menu - given menu name.
*Tag draw_menu will draw a tree menu based on the elements created in the admin panel.

