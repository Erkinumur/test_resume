from django.urls import path

from .views import ResumeCreateView, success_create

urlpatterns = [
    path('create/', ResumeCreateView.as_view(), name='resume_create'),
    path('create/success/', success_create, name='resume_success'),
]