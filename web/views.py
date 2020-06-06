# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def index(request):
    return render(request,'demo.html')

def current_time(request):
    return render(request,'ct.html',{'a':int(time.time()), 'b': time.strftime("%A,%B %d,%Y %H:%M:%S %p GMT %z", time.localtime())})