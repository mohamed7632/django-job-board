from django.shortcuts import render,redirect
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm,JobForm
from django.urls import reverse
# Create your views here.
def job_list(request):
    job_list=Job.objects.all()
    paginator = Paginator(job_list, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj}
    return render(request,'Job/job_list.html',context)


def job_detail(request,slug):
    job=Job.objects.get(slug=slug)
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job
            myform.save()
    else:
        form=ApplyForm()
    context={'job':job,'form':form}
    return render(request,'Job/job_details.html',context)
#apply on job  function
def add_job(request):
    if request.method=='POST':
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form=JobForm()
    context={'form':form}
    return render(request,'Job/add_job.html',context)
