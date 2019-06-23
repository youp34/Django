from django.shortcuts import render, redirect,HttpResponse
from app import models
from django import views
import json

# Create your views here.
def logout(request):
    request.session.clear()
    return redirect('/login.html')

def login(request):
    message=""
    #v = request.session
    #from django.contrib.sessions.backends.db import SessionStore
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = models.User.objects.filter(user=user,pwd=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = "用户名或密码错误请重新输入！"

    return render(request,'login.html',{"msg": message})
def index(request):
    username = request.session.get('username')
    a=request.session['is_login']
    if username and a:
        return render(request ,"index.html", {'user':username})
    else:
        return redirect('/login.html')

import os
def upload (request):
    username = request.session.get('username')
    a=request.session['is_login']
    if username and a:
       # models.Img.objects.filter(id=12).delete()
        if request.method == 'GET':
            img_list = models.Img.objects.all()
            return render(request, 'upload.html', {'img_list': img_list})
        elif request.method == "POST":
            fafafa = request.POST.get('fafafa')
            obj = request.FILES.get('fafafa')
            file_path = os.path.join('static', 'upload', obj.name)     #拼接路径
            f = open(file_path, 'wb')
            for chunk in obj.chunks():
                f.write(chunk)
            f.close()
            models.Img.objects.create(path=file_path)
            return redirect('/upload.html')
    else:
        return redirect('/login.html')

