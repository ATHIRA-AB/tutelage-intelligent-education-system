"""guru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from guruapp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,name="index"),
    url(r'^index/$',index,name="index"),
    url(r'^login/$',login,name="login"),
    url(r'^chatbot/$',chatbot,name="chatbot"),
    url(r'^slogaction/$',slogaction,name="slogaction"),
    url(r'^logaction/$',logaction,name="logaction"),
    url(r'^Course/$',Course,name="Course"),
    url(r'^courseaction/$',courseaction,name="courseaction"),
    url(r'^delcou/$',delcou,name="delcou"),
    url(r'^department/$',department,name="department"),
    url(r'^deptaction/$',deptaction,name="deptaction"),
    url(r'^deldpt/$',deldpt,name="deldpt"),
    url(r'^Faculty/$',Faculty,name="Faculty"),
    url(r'^facaction/$',facaction,name="facaction"),
    url(r'^delfac/$',delfac,name="delfac"),
    url(r'^student/$',student,name="student"),
    url(r'^studaction/$',studaction,name="studaction"),
    url(r'^Subject/$',Subject,name="Subject"),
    url(r'^subaction/$',subaction,name="subaction"),
    url(r'^delsub/$',delsub,name="delsub"),
    url(r'^vstudent/$',vstudent,name="vstudent"),
    url(r'^fvstudent/$',fvstudent,name="fvstudent"),
    url(r'^fvstudent1/$',fvstudent1,name="fvstudent1"),
    url(r'^fvatt1/$',fvatt1,name="fvatt1"),
    url(r'^notes/$',notes,name="notes"),
    url(r'^noteaction/$',noteaction,name="noteaction"),
    url(r'^vnotes/$',vnotes,name="vnotes"),
    url(r'^adqns/$',adqns,name="adqns"),
    url(r'^vqns/$',vqns,name="vqns"),
    url(r'^chat/$',chat,name="chat"),
    url(r'^chataction/$',chataction,name="chataction"),
    url(r'^vchat/$',vchat,name="vchat"),
    url(r'^vchataction/$',vchataction,name="vchataction"),
    url(r'^ansaction/$',ansaction,name="ansaction"),
    url(r'^qnaction/$',qnaction,name="qnaction"),
    url(r'^vcourse/$',vcourse,name="vcourse"),
    url(r'^vsubject/$',vsubject,name="vsubject"),
    url(r'^Timetable/$',Timetable,name="Timetable"),
    url(r'^timeaction/$',timeaction,name="timeaction"),
    url(r'^vtimetable/$',vtimetable,name="vtimetable"),
    url(r'^svtimetable/$',svtimetable,name="svtimetable"),
    url(r'^stvtimetable/$',stvtimetable,name="stvtimetable"),
    url(r'^delnot/$',delnot,name="delnot"),
    url(r'^delqns/$',delqns,name="delqns"),
    url(r'^attaction/$',attaction,name="attaction"),
    url(r'^studentHome/$',studentHome,name="studentHome"),
    url(r'^facultyHome/$',facultyHome,name="facultyHome"),
    url(r'^adminHome/$',adminHome,name="adminHome"),
    # url(r'^index/$',TemplateView.as_view(template_name='index.html')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=staticfiles_urlpatterns()
