from django.shortcuts import render
from . models import Job
from django.core.paginator import Paginator
# Create your views here.


def job_list(request):
    jobs = Job.objects.all()

    paginator = Paginator(jobs, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
    }
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job = Job.objects.get(slug=slug)
    context = {
        'job': job,
    }
    return render(request, 'job/job_detail.html', context)