from django.urls import path
from . import views


urlpatterns = [
    path('',views.studata, name='studata'),
    path('student/<int:id>',views.studatafind, name='studatafind')
]