Для запуска приложения потребуется:
1. Скопировать репозиторий: https://github.com/Vicki-art/UpTrader_test.git;
2. Установить Django(4.2.3) и python (ver=3.11), при необходимости;
3. Применить миграции и запустить сервер:
   python3 manage.py migrate
   python3 manage.py runserver

Использование
Создание меню
Меню можно создавать через стандартную админку Django. Для этого нужно зайти на страницу http://127.0.0.1:8000/admin/menu_tree/menu/, где http://localhost:8000 - адрес вашего приложения.
На этой странице вы можете создать новое меню, задав ему название и uri. 
Элементы меню можно создавать в так же в админке Django. Для этого нужно зайти на страницу http://127.0.0.1:8000/admin/menu_tree/submenu/.

Отображение меню
Чтобы отобразить меню на странице, нужно загрузить template tag:
{% load menu_tags %}

И затем в нужном месте вызвать
{% draw_menu 'requested_menu' %}
где requested_menu - название меню.
Тег draw_menu будет рисовать древовидное меню, основываясь на элементах, созданных в админке.

