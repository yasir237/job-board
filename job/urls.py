from django.contrib import admin
from django.urls import path, include

from .views import job_list, job_detail, job_add
app_name = 'jobs'

urlpatterns = [
    # for get all jobs
    path('', job_list, name='job_list'),
    path('list/', job_list, name='job_list'),

    # for add job
    path('add/', job_add, name='job_add'),

    # for get job by id
    path('<str:slug>/', job_detail, name='job_detail'),
    path('detail/<str:slug>/', job_detail, name='job_detail'),


    
]
