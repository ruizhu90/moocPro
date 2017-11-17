# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import UserMessage

# Create your views here.
# 注册
def getform(request):

    if request.method == "POST":
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.password = password
        user_message.save()

    return render(request,'sign_up.html')

# 登陆
def login(request):

    return render(request, 'log_in.html')