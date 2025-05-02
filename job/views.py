from django.shortcuts import render

# Create your views here.

def job_list(request):
    return render(request, 'job/job_list.html')


def job_detail(request, id):
    return render(request, 'job/job_detail.html', {'id': id})