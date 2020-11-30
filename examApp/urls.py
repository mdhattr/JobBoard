from django.urls import path
from . import views

urlpatterns=[
    path('', views.root),
    path('process_registration', views.process_registration),
    path('process_login', views.process_login),
]