from django.urls import path, include
from django.contrib import admin
from menu_tree import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<path:current_uri>', views.demo, name = 'demo')
]
