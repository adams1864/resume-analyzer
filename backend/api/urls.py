from django.urls import path
from . import views

urlpatterns = [
    path('auth/login', views.login),
    path('upload', views.upload_resume),
    path('extract_pdf/', views.extract_pdf, name='extract_pdf'),
]
