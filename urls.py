# -*- coding: utf-8 -*- 
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from django.conf import settings
from gallery import views

urlpatterns = [
    url(r'^$', views.gallery, name='gallery'),
    url(r'^album-(?P<id_root>[-\w]+).html', views.gallery_album, name='gallery_album'),
    url(r'^album-(?P<id_root>[-\w]+)/photo-(?P<id_album>[-\w]+).html', views.gallery_foto, name='gallery_foto'),
]