from django.contrib import admin
from django.urls import include, path

from CINExtract.views import CIN_View

urlpatterns = [
    path('cin', CIN_View.as_view(), name='cin')
]
