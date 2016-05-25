# coding:utf8
from django.conf.urls import patterns, url

urlpatterns = patterns('usercenter',
                       url(r'^index/$', 'views.index'),
                       )