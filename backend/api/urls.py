from django.urls import path
from .views import login, upload_resume

urlpatterns = [
    path('auth/login', login),
    path('upload', upload_resume),
]
