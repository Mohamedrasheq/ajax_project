from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index_page"),
    path('create',views.create,name="create_object"),
    path('disp_profile/',views.profile_view,name="get_from_database"),
    path('get-profiles/',views.getdata,name="html_page")
]