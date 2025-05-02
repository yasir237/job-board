from django.contrib import admin
from django.urls import path, include

from .views import job_list, job_detail

urlpatterns = [
    # for get all jobs
    path('', job_list, name='job_list'),
    path('list/', job_list, name='job_list'),

    # for get job by id
    path('<int:id>/', job_detail, name='job_detail'),
    path('detail/<int:id>/', job_detail, name='job_detail'),
]
