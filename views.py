# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connection
from django.shortcuts import render, redirect
from django.shortcuts import render
from  django.shortcuts import HttpResponse,HttpResponseRedirect
import pymysql
# Create your views here.
from django.shortcuts import HttpResponse

db = pymysql.connect(host="127.0.0.1", user="root", password='', db="project_display")
from django.contrib  import  auth#引入auth模块

from django.contrib.auth.models import User # auth应用中引入User类
user_list = []


def index(request):
    if request.method == "GET":
        return HttpResponse('这是首页')


def dashboard(request):
    if request.method == "GET":
        username = ""
        admin_name = ""
        stu = User.objects.filter(is_superuser=0).order_by("id")
        admin = User.objects.filter(is_superuser=1).order_by("id")
        for items in admin:
            admin_name += admin.username
        username = admin_name
        return render(request, "dashboard.html", {'admin_info': username})

def login(request):
    # # check if the user is already loged in
    # if request.user.is_authenticated:
    #     return redirect(request.META.get('HTTP_REFERER', '/'))
    # else:
    #     if request.method == "GET":
    #         return render(request, "login.html")
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(password)
        if username != "" and password != "":
            username = username.strip()
            try:
                user = User.objects.get(username = username)
            except:
                return render(request, '/LoginFail/')
            if user.password == password:
                print("fuck")
                return redirect('/myProfile/')
            else:
                print(password)
                print(user.password)
                return redirect('/LoginFail/')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'GET':
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        return render(request, 'signup.html', locals())
    else:
        #get the result from the form in HTML
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username != "" and password != "" :
            if User.objects.filter(username = username).exists() == False:
                #register a new user if do not exist a current one
                user = User.objects.create_user(username = username,password = password)
                user.save()
                user_info = {"username": user.username}
                # 登录
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                #login(request, user)
                # 重定向跳转
                return redirect('/login/')
        else:
            return render(request, 'LoginFail.html')
    return render(request, 'signup.html')


def signupSuccess(reqest):
    if reqest.method == "GET":
        return render(reqest, 'signupSuccess.html')

def LoginFail(request):
    if request.method == "GET":
        return render(request, "LoginFail.html")


def myProfile(request):
    if request.method == "GET":
        return render(request, "myProfile.html")


def myWorks(request):
    if request.method == "GET":
        return render(request, "myWorks.html")

