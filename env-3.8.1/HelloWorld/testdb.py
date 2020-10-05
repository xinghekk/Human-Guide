# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Truth
from django.shortcuts import render
#建立Truth模型，获取Truth数据
#添加数据
def testdb(request):
   id=request.GET.get("id")
   Truth=request.GET.get("Truth")
   reason=request.GET.get("reason")
   Truth1=Truth(id=id,Truth=Truth,reason=reason)
   Truth1.save()
   return HttpResponse("<p>数据添加成功！</p>")
#输出所有数据

