from web_app import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', views.userInfo, name = 'userInfo'),
]
