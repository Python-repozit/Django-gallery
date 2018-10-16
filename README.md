# Django-gallery
Django-gallery module with multi-load widget

Исполняемые файлы папка gallery
Папка со страницами шаблона templates

Подключаем модуль в settings.py:
    INSTALLED_APPS = [
      'gallery',
  ]

Не забываем в корневой файл urls.py добавить подключение:
  url(r'^gallery/', include('gallery.urls')),
  
 
 *Работает с ресайз изображениями на основе django_resized : https://github.com/un1t/django-resized
