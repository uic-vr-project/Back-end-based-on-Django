# -*- coding: utf-8 -*-
# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import redirect, render
import pymysql
from django.shortcuts import HttpResponse
from Gallery_app.models import threeDmodel, Video, OilPaint
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
db = pymysql.connect(host="127.0.0.1", user="root", password='', db="project_display")



def index(request):
    if request.method == "GET":
        return HttpResponse('这是首页')


def dashboard(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            admin_name = request.user.username
            paint = OilPaint.objects.all()
            model = threeDmodel.objects.all()
            video = Video.objects.all()
            paint_num = 0
            video_num = 0
            model_num = 0
            for item in paint:
                paint_num += 1

            for item in video:
                video_num += 1

            for item in model:
                model_num += 1

            total_num = paint_num + video_num + model_num
        else:
            return redirect('login time out, pls login')
    return render(request, 'dashboard.html', {'total_num': total_num, 'paint_num':paint_num,
                                              'video_num': video_num,'model_num': model_num,
                                              'admin_name': admin_name, 'OilPaint_info': paint,
                                              'model_info': model, 'video_info': video})


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username != "" and password != "":
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)#auth下的login() 方法，就相当于session+cookie
                if request.user.is_superuser:
                    return redirect('/dashboard/')
                else:
                    return redirect('/myProfile/')
            else:
                return redirect('/LoginFail/')
        else:
            return HttpResponse("fill in all the blanks")
    return render(request, 'login.html')

def signup(request):
    if request.method == 'GET':
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        return render(request, 'signup.html', locals())
    else:
        #get the result from the form in HTML
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPsw = request.POST.get('confirmPsw')
        if username != "" and password != "" and confirmPsw != "":
            if password == confirmPsw:
                if User.objects.filter(username=username).exists() == False:
                    # register a new user if do not exist a current one
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    user_info = {"username": user.username}
                    # 登录
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    # login(request, user)
                    # 重定向跳转
                    return render(request, 'signupSuccess.html', {'username':username})
                else:
                    return HttpResponse("this user already exist, pls login")
            else:
                return redirect('/confirmFail/')
        else:
            return HttpResponse("fill in all the blanks")
    return render(request, 'signup.html')

def myProfile(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            paint_num = 0
            video_num = 0
            model_num = 0

            paint = OilPaint.objects.filter(author=request.user.username)
            video = Video.objects.filter(author=request.user.username)
            model = threeDmodel.objects.filter(author=request.user.username)
            for item in paint:
                paint_num += 1

            for item in video:
                video_num += 1

            for item in model:
                model_num += 1

            total_num = paint_num+video_num+model_num
            return render(request, "myProfile.html", {'user_name': request.user.username,'paint_num': paint_num,
                                                      'video_num': video_num,'model_num': model_num,
                                                      'total_num': total_num})
        else:
            return redirect('/LoginFail/')

def myWorks(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            paint = OilPaint.objects.filter(author=request.user.username)
            model = threeDmodel.objects.filter(author=request.user.username)
            video = Video.objects.filter(author=request.user.username)
        else:
            return redirect('/LoginFail/')
    return render(request, 'myWorks.html', {'OilPaint_info': paint, 'model_info': model, 'video_info': video})

def newWork(request, type):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'newWork.html')
        else:
            return redirect('/LoginFail/')
    else:
        if request.user.is_authenticated:
            # get the work information from templates
            author = request.user.username
            name_of_work = request.POST.get('name')
            teacher = request.POST.get('teacher')
            series = request.POST.get('series')
            description = request.POST.get('description')
            if name_of_work != "" and author != "" and teacher != "" and series != "" and description != "":

                if type == 'Oil_Paint':
                    if OilPaint.objects.filter(name=name_of_work).exists() == False:
                        paint = OilPaint.objects.create(name=name_of_work, author=author, teacher=teacher, series=series,
                                                 description=description, type=type)
                        paint.save()
                        return redirect('/myWorks/')
                    else:
                        return HttpResponse("you already have this work")
                elif type == '3D_model':
                    if threeDmodel.objects.filter(name=name_of_work).exists() == False:
                        model = threeDmodel.objects.create(name=name_of_work, author=author, teacher=teacher, series=series,
                                                 description=description, type=type)
                        model.save()
                        return redirect('/myWorks/')
                    else:
                        return HttpResponse("you already have this work")
                elif type == 'Video':
                    if Video.objects.filter(name=name_of_work).exists() == False:
                        video = Video.objects.create(name=name_of_work, author=author, teacher=teacher, series=series,
                                                 description=description, type=type)
                        video.save()
                        return redirect('/myWorks/')
                    else:
                        return HttpResponse("you already have this work")

    return render(request, 'newWork.html')

def changePwd(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "changePwd.html")
        else:
            return redirect('/LoginFail/')
    else:
        if request.user.is_authenticated:
            oldPwd = request.POST.get('oldPwd')
            newPwd = request.POST.get('newPwd')
            if oldPwd != "" and newPwd != "":
                user = User.objects.get(username=request.user.username)

                if user.check_password(oldPwd):
                    user.set_password(newPwd)
                    user.save()
                    return redirect('/myProfile/')
                else:
                    return redirect('/confirmFail/')
        else:
            return redirect('/LoginFail/')
    return render(request, 'changePwd.html')

def logout(reqeust):
    if reqeust.method == "GET":
        reqeust.session.flush()
        return redirect('/login/')
    return render(reqeust, 'login.html')


def deleteConfirm(request,name, id, type):
    if request.user.is_authenticated:
        return render(request, 'deleteConfirm.html', {'name': name, 'ID': id, 'type': type})
    else:
        return redirect('/LoginFail/')




def delete(request, name, id, type):
    if request.user.is_authenticated:
        if type == 'Oil_Paint':
            paint = OilPaint.objects.filter(id=id)
            paint.delete()
        elif type == '3D_model':
            model = threeDmodel.objects.filter(id=id)
            model.delete()
        elif type == 'Video':
            video = Video.objects.filter(id=id)
            video.delete()
            if request.user.is_superuser:
                return redirect('/dashboard/')
            else:
                return redirect('/myProfile/')
    else:
        return redirect('/LoginFail/')
    if request.user.is_superuser:
        return redirect('/dashboard/')
    else:
        return redirect('/myProfile/')


def modifyConfirm(request, id, type):
    if request.method == "GET":

        if request.user.is_authenticated:
            return render(request, "modifyPage.html")
        else:
            return redirect('/LoginFail/')
    else:
        if request.user.is_authenticated:
            if id:
                # get the work information from templates
                name_of_work = request.POST.get('name')
                teacher = request.POST.get('teacher')
                series = request.POST.get('series')
                description = request.POST.get('description')
                if name_of_work != "" and teacher != "" and series != "" and description != "":

                    if type == 'Oil_Paint':
                        paint = OilPaint.objects.get(id=id)
                        paint.name = name_of_work
                        paint.teacher = teacher
                        paint.series = series
                        paint.description = description
                        paint.save()
                    elif type == '3D_model':
                        model = threeDmodel.objects.get(id=id)
                        model.name = name_of_work
                        model.teacher = teacher
                        model.series = series
                        model.description = description
                        model.save()
                    elif type == 'Video':
                        video = Video.objects.get(id=id)
                        video.name = name_of_work
                        video.teacher = teacher
                        video.series = series
                        video.description = description
                        video.save()
                    if request.user.is_superuser:
                        return redirect('/dashboard/')
                    else:
                        return redirect('/myProfile/')
                else:
                    return HttpResponse("you must fill in all of these")
        else:
            return redirect('/LoginFail/')
    return render(request, 'modifyPage.html')

def signupSuccess(request):
    if request.method == "GET":
        return render(request, 'signupSuccess.html')

def LoginFail(request):
    if request.method == "GET":
        return render(request, "LoginFail.html")


def confirmFail(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "confirmFail.html")
        else:
            return redirect('/LoginFail/')

def typeConfirm(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "typeConfirm.html")
        else:
            return redirect('/LoginFail/')





