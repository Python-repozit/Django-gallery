#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.contrib import admin
from widgets import MultiFileInput
from django import forms
from gallery.models import *
from django.http import HttpResponseRedirect, HttpResponse

class RootAlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_img', 'order')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'root', 'image_img', 'order')

class PhotoAdminForm(forms.ModelForm):
 
    class Meta:
        model = Photo
        fields = ['album', 'title', 'file', 'order']
        widgets = {'file':MultiFileInput}
 
class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminForm

    def add_view(self, request, *args, **kwargs):
        files = request.FILES.getlist('file',[])
        is_valid = PhotoAdminForm(request.POST, request.FILES).is_valid()
 
        if request.method == 'GET' or len(files)<=1 or not is_valid:
            return super(PhotoAdmin, self).add_view(request, *args, **kwargs)
        for file in files:
            number=['id'] 
            album_id=request.POST['album']
            title = request.POST['title']
            try:
                photo = Photo(title=title, album_id=album_id, file=file)
                photo.save()
            except Exception, e:
                messages.error(request, smart_str(e))
 
        return HttpResponseRedirect('/admin/gallery/photo/')

    list_display = ('title', 'album', 'image_img', 'order')
    search_fields = ['album', 'title']
    list_filter = ('album', 'title')

admin.site.register(RootAlbum, RootAlbumAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
