from django.shortcuts import redirect, render
from . models import Job
from django.core.paginator import Paginator
from .form import ApplyForm, JobForm
# Create your views here.


def job_list(request):
    jobs = Job.objects.all()

    paginator = Paginator(jobs, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
    }
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job = Job.objects.get(slug=slug)


    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit= False)
            myform.job = job
            myform.save()

    else:
        form = ApplyForm()


    context = {
        'job': job,
        'form_to_apply': form,
    }
    return render(request, 'job/job_detail.html', context)


def job_add(request):
    
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.owner = request.user
            job.save()
            return redirect('jobs:job_list')

    else:
        form = JobForm()


    context = {
        'form_add': form,
    }

    return render(request, 'job/job_add.html',context)