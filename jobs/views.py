from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm

@login_required(login_url='/login/')
def index(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/index.html', {'jobs': jobs})

@login_required(login_url='/login/')
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})

@login_required(login_url='/login/')
def delete_job(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect('index')

@login_required(login_url='/login/')
def update_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/update_job.html', {'form': form})