from task1 import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.userlogin, name='login'),
    path('signup/', views.usersignup, name='signup'),
    path('log/', views.userlogout, name='logout'),
    path('add_data/', views.addstudent, name='add'),
    path('update/<int:id>', views.updatestudent, name='changedata'),
    path('delete/<int:id>', views.deletestudent, name='deletedata'),
    path('search/', views.searchstudent, name='search'),
    path('help/', views.contact, name='help')
]
