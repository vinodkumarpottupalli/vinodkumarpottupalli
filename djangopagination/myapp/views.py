from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Job
from .forms import NewJobPostForm
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


JOBS_PER_PAGE = 10

# Create your views here.
def index(request):
    
    search_query = ''
    search_location = ''
    search_type = ''
    if request.GET.get('q'):
        search_query = request.GET.get('q')
 
    if request.GET.get('location'):
      search_location = request.GET.get('location')
     
    if request.GET.get('type'):
      search_type = request.GET.get('type')

    jobs = Job.objects.filter(title__icontains=search_query, location__icontains=search_location, type__icontains=search_type)

    # Pagination
    page = request.GET.get('page',1)
    job_paginator = Paginator(jobs, JOBS_PER_PAGE)

    try:
      jobs = job_paginator.page(page)
    except PageNotAnInteger:
      jobs = job_paginator.page(JOBS_PER_PAGE)
    except EmptyPage:
      jobs = job_paginator.page(job_paginator.num_pages)


    index = job_paginator.page_range.index(jobs.number)
    max_index = len(job_paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = job_paginator.page_range[start_index:end_index]

    type_values = Job.objects.order_by().values('type').distinct()
    location_values = Job.objects.order_by().values('location').distinct()

    context = {'jobs':jobs, 'query':search_query, 'query_location':search_location, 
                'query_type':search_type,'type_values':type_values, 'location_values':location_values,
                'page_range': page_range}
    return render(request, 'index.html', context)


def view_job(request, pk):
    job = Job.objects.get(id=pk)
    context = {'job':job}
    return render(request, 'view-job.html', context)


def createPost(request):
    form = NewJobPostForm()
    if request.method == 'POST':
        form = NewJobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"job_post_form":form}
    return render(request, 'create-post.html', context)
