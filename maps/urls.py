#
#   TUTORIAL INSTRUCTS THIS: 
#   from django.conf.urls import url  
#   BUT...
#   django.conf.urls.url() was deprecated in Django 3.0,
#   and is removed in Django 4.0+
#
  
"""
Created on Fri Feb 10 15:50:09 2023

URLS for MAPS App

@author: ali_d
"""

from django.urls import include, re_path
#   recommended fix is re_path deom stack overflow~
#   Alternatively, you could switch to using path. path() does not use regexes,
#   so you'll have to update your URL patterns if you switch to path.


from . import views

urlpatterns = [ 
    re_path(r'', views.default_map, name="default"),
    #path('', views.default_map, name="default"),#this doesnt work

]