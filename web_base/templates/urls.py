
from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', views.index,name="index"),
    path('landing/',views.landing_page, name='landing')
    
]
