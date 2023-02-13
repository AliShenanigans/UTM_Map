# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:50:09 2023

URLS for Addresses App

@author: ali_d
"""

from django.urls import path
from .views import AddressView


urlpatterns = [
    #re_path(r'', AddressView.as_view(), name='home'),#doesnt work...
    path('', AddressView.as_view(), name='home'),

]