# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        "date":datetime.today().date(),
        "time":datetime.today().time()
    }
    return render(request, "timeApp/index.html", context)