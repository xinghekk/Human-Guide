
from django.conf.urls import url
from django.urls import path
from .import views,testdb
from django.contrib import admin
 
from . import views
 
urlpatterns = [
    path('runoob/',views.runoob),
   path('testdb/', views.list),
    path('index/',views.index),
    url(r'^admin/',admin.site.urls),
]

