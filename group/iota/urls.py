from django.urls import path
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views 

urlpatterns = [

    path('', views.home, name = 'home'),
    path('urja', views.urja, name = 'urja'),
    path('register',views.register,name = 'register'),
    path('log_in',views.log_in,name='log_in'),
    path('about_us',views.about_us,name = 'about_us'),
    path('user_data',views.user_data,name = 'user_data'),
]