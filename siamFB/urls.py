"""siamFB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from status.views import home_view,detailed_status,status_list_view
from crud.views import student_view,single_student_view,create_student,StudentApi,create_student_form

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',home_view),
    path('status/<int:status_id>',detailed_status),
    path('status',status_list_view),
    path('students',student_view),
    path('students/<int:id>',student_view),
    path('student-classbased-view',StudentApi.as_view()),
    path('student-classbased-view/<int:id>', StudentApi.as_view()),

    path('student-create',student_view),
    path('student-create-form',create_student_form)
]
