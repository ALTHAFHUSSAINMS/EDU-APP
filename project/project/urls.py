"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display),
    path('student', views.display1),
    path('college', views.display2),
    path('create', views.create),
    path('create1', views.create1),
    path('login', views.display3),
    path('log', views.log),
    path('profile', views.profile),
    path('profile1', views.profile1),
    path('science1', views.science1),
    path('commerce1', views.commerce1),
    path('literature1', views.literature1),
    path('humanities1', views.humanities1),
    path('finearts1', views.finearts1),
    path('journalism1', views.journalism1),
    path('engineering1', views.engineering1),
    path('law1', views.law1),
    path('sub1', views.sub1),
    path('sub2', views.sub2),
    path('sub3', views.sub3),
    path('sub4', views.sub4),
    path('sub5', views.sub5),
    path('sub6', views.sub6),
    path('sub7', views.sub7),
    path('sub8', views.sub8),
    path('find', views.find),
    path('edit', views.edit),
    path('update', views.update),
    path('edit1', views.edit1),
    path('update1', views.update1),
    path('delete', views.delete),
    path('view1', views.SUB1),
    path('view2', views.SUB2),
    path('view3', views.SUB3),
    path('view4', views.SUB4),
    path('view5', views.SUB5),
    path('view6', views.SUB6),
    path('view7', views.SUB7),
    path('view8', views.SUB8),
    path('s1delete', views.s1delete),
]
