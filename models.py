#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.db import models
from datetime import *
from django import forms
from django_resized import ResizedImageField
#from multiupload.fields import MultiFileField

class RootAlbum(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название корневого альбома')
    image = ResizedImageField(size=[250, 250], upload_to='Photo_category', help_text='250x250px', verbose_name='Картинка')
    order = models.CharField(max_length=100, verbose_name='Порядок отображения(От 1 до..)', default='')

    class Meta:
        verbose_name = "Корневая категория"
        verbose_name_plural = "Корневая категория"

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.name

    def delete(self, using=None):        
        try:
            obj = RootAlbum.objects.get(pk=self.pk)
            obj.image.delete()
        except (RootAlbum.DoesNotExist, ValueError):
            pass
        super(RootAlbum, self).delete()

class Album(models.Model):
    root = models.ForeignKey(RootAlbum, verbose_name='Корневая категория', default='')
    name = models.CharField(max_length=100, verbose_name='Название дочернего альбома')
    image = ResizedImageField(size=[250, 250], upload_to='Photo_category', help_text='250x250px', verbose_name='Картинка категории')
    order = models.CharField(max_length=100, verbose_name='Порядок отображения(От 1 до..)', default='')

    class Meta:
        verbose_name = "Дочерняя категория"
        verbose_name_plural = "Дочерняя категория"

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    def delete(self, using=None):        
        try:
            obj = Album.objects.get(pk=self.pk)
            obj.image.delete()
        except (Album.DoesNotExist, ValueError):
            pass
        super(Album, self).delete()

    def __unicode__(self):
        return self.name

class Photo(models.Model):
    album = models.ForeignKey(Album, verbose_name='Дочерняя категория')
    title = models.CharField(max_length=255, blank=True, default='', verbose_name='Фото')
    file = ResizedImageField(size=[800, 800], crop=['middle', 'center'], upload_to='Photogallery', verbose_name='Фотографии')
    order = models.CharField(max_length=100, blank=True, verbose_name='Порядок отображения(От 1 до..)', default='')

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

    def image_img(self):
        if self.file:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.file.url)
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    def delete(self, using=None):        
        try:
            obj = Photo.objects.get(pk=self.pk)
            obj.file.delete()
        except (Photo.DoesNotExist, ValueError):
            pass
        super(Photo, self).delete()

    def get_absolute_url(self):
        return self.file.url

    def __unicode__(self):
        return self.title