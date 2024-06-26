from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path("",views.home,name="home"),
    path("checklogin",views.checklogin,name="checklogin"),
    path("insertsite",views.insertsite,name="insertsite"),
    path('display-property', views.display_property_information, name='display_property'),
    path('firstpage',views.firstpage,name='firstpage'),
    path('signup',views.signup,name='signup'),
    path('registeruser',views.registeruser,name='registeruser')
]