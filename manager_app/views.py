# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connection
from django.shortcuts import render
from django.shortcuts import render
from  django.shortcuts import HttpResponse,HttpResponseRedirect
import pymysql
# Create your views here.
from django.shortcuts import HttpResponse

db = pymysql.connect(host="127.0.0.1", user="root", password='', db="project_display")

user_list = []


def dashboard(request):
    #return HttpResponse('hello fuckers !~')
    return render(request,'dashboard.html')

def login(request):
    if request.method == "POST":
        (userName) = request.POST.get("username")
        passWord = request.POST.get("password")
        curAdmin = db.cursor()
        curAdmin.execute('select * from admin')
        admin_info = curAdmin.fetchall()
        curStu = db.cursor()
        curStu.execute('select name,pwd from login')

        stu_info = curStu.fetchall()

        print(admin_info)
        print(stu_info)
        print(userName, passWord)
        if (userName, passWord) in admin_info:
            print("goodAdmin")
            request.session['is_login'] = True
            request.session['username'] = userName
            return render(request, "dashboard.html")
        elif (userName, passWord) in stu_info:
            print("goodStu")
            request.session['is_login'] = True
            request.session['username'] = userName
            #return myProfile(request,userName)
            return myWorks(request, userName)
        else:
            return render(request, "LoginFail.html")

    if request.method == "GET":
        request.session['is_login'] = False
        return render(request, "login.html")
    return render(request,"login.html")


def signup(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        confirmPsw = request.POST.get('confirmPsw')
        print(userName,passWord,confirmPsw)
        temp = {'user': userName,"psw": passWord}
        user_list.append(temp)
    return render(request,'signup.html',{'userData':user_list})

def signupSuccess(request):
    return render(request,'signupSuccess.html')


def LoginFail(request):
    return render(request, "LoginFail.html")


def myProfile(request,userName):
    if request.method == "POST":
        stu_info = []
        curStuName = db.cursor()
        curStuPwd = db.cursor()
        curStuDep = db.cursor()
        curMail = db.cursor()

        curStuName.execute('select name from login where name=%s', userName)
        stu_Name_fetch = curStuName.fetchall()
        print(stu_Name_fetch)

        curStuPwd.execute('select pwd from login where name=%s', userName)
        stu_Pwd_fetch = curStuPwd.fetchall()
        print(stu_Pwd_fetch)

        curStuDep.execute('select dep from login where name=%s', userName)
        stu_Dep_fetch = curStuDep.fetchall()
        print(stu_Dep_fetch)

        curMail.execute('select mail from login where name=%s', userName)
        stu_Mail_fetch = curMail.fetchall()
        print(stu_Mail_fetch)

        temp = {'stuName': stu_Name_fetch, 'stuPwd': stu_Pwd_fetch, 'stuDep': stu_Dep_fetch, 'stuMail': stu_Mail_fetch}
        stu_info.append(temp)

    return render(request, "myProfile.html", {'stu_info': stu_info})


def myWorks(request, userName):
    if request.method == "POST":
        curWorkName = db.cursor()
        curWorkLocation = db.cursor()
        curWorkClass = db.cursor()
        curWorkSchool = db.cursor()
        curID = db.cursor()
        curAll = db.cursor()

        curWorkName.execute('select workName from work where userName=%s', userName)
        work_Name_fetch = curWorkName.fetchall()
        print(work_Name_fetch)

        curWorkLocation.execute('select Location from work where userName=%s', userName)
        work_Location_fetch = curWorkLocation.fetchall()
        print(work_Location_fetch)

        curWorkClass.execute('select class from work where userName=%s', userName)
        work_Class_fetch = curWorkClass.fetchall()
        print(work_Class_fetch)


        curWorkSchool.execute('select school from work where userName=%s', userName)
        work_School_fetch = curWorkSchool.fetchall()
        print(work_School_fetch)


        curID.execute('select id from work where userName=%s', userName)
        work_ID_fetch = curID.fetchall()

        curAll.execute('select * from work')
        allFetch = curAll.fetchall()
        print(allFetch)


        temp = {'workID': work_ID_fetch,'userName': userName,'workName': work_Name_fetch,
                'workLocation': work_Location_fetch, 'workClass':
                    work_Class_fetch,'workSchool': work_School_fetch}
        works_info = []
        works_info.append(temp)

    return render(request, "myWorks.html", {'parem': works_info})

