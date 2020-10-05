from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Truth
def runoob(request):
    context ={}
    context['hello']='Hello World!'
    return render(request,'runoob.html',context)
def index(request):
    Truth_list=[[1,2,3],[4,5,6]]
    return render(request,'index.html',{"Truth_list":Truth_list})
def list(request):
    list1=Truth.objects.values()
    return render(request,'list.html',{"list":list1})


