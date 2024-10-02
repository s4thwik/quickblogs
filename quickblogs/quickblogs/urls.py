"""
URL configuration for quickblogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home1),
    path('1',views.login1),
    path('2', views.reg1),
    path('3', views.viewvlogs1),
    path('4', views.myvlogs1),
    path('5', views.register),
    path('6', views.userprofile),
    path('7', views.newpost),
    path('8', views.login),
    path('9', views.publishpost),
    path('9', views.publishpost),
    path('10', views.logout),
    path('11', views.read),
    path('12', views.editvlog),
    path('13', views.editbtn),
    path('14', views.deletebtn),
    path('15', views.goprofile),
    path('16', views.editprofile),
    path('0',views.home1),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)