from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.template.context_processors import csrf
from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import  redirect
from django.utils.encoding import smart_str
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gallery.models import *
from django import forms
import random
import string

def gallery(request):

	root = RootAlbum.objects.filter().order_by('order')

	context = {
		'root' : root,
	}
	return render(request, 'gallery/gallery.html', context)

def gallery_album(request, id_root):

	album = Album.objects.filter(root=id_root).order_by('-order')
	paginator = Paginator(album, 8)
	page = request.GET.get('page')
	try:
		album = paginator.page(page)
	except PageNotAnInteger:
		album = paginator.page(1)
	except EmptyPage:
		album = paginator.page(paginator.num_pages)

	context = {
		'album' : album,
		'page': page, 
	}
	return render(request, 'gallery/gallery_album.html', context)

def gallery_foto(request, id_root, id_album):

	album = Album.objects.filter(root=id_root)
	photo = Photo.objects.filter(album=id_album).order_by('order')
	paginator = Paginator(photo, 6)
	page = request.GET.get('page')
	try:
		photo = paginator.page(page)
	except PageNotAnInteger:
		photo = paginator.page(1)
	except EmptyPage:
		photo = paginator.page(paginator.num_pages)

	context = {
		'photo' : photo,
		'page': page,
	}
	return render(request, 'gallery/gallery_foto.html', context)