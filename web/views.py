# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import time
import tzlocal
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'demo.html')

def current_time(request):
    return render(request,'ct.html',{'a':int(time.time()), 'b': datetime.fromtimestamp(time.time(), tzlocal.get_localzone()).strftime("%A,%B %d,%Y %H:%M:%S %p %Z %z")})