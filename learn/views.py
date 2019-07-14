# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# def index(request):
#     return HttpResponse(u"Hello World!")

# def index(request):
#     string = u'Are You Ok!'
#     return render(request, 'home.html', {'string': string})

def home(request):
    string = 'Are You Ok!'
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    List = map(str, range(100))# 一个长度为100的 List
    return render(request, 'home.html', {'TutorialList': TutorialList, 'string': string , \
    'info_dict': info_dict , 'List': List})

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )
