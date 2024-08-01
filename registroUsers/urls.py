from django.contrib import admin
from django.urls import path
from registroUsers import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.signout,name='logout'),
    path('login/',views.signin,name='login'),
]