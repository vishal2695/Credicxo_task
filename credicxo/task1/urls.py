from task1 import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userlogin, name='login'),
    path('signup/', views.usersignup, name='signup'),
    path('log/', views.userlogout, name='logout')
]
