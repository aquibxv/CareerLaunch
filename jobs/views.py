from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JobApplied, Job

# Create your views here.
def application(request, job_id):
    """View for applied job applications """

    # check if candidate has already applied to this job
    has_applied = JobApplied.objects.all().filter(candidate=request.user, job_id=job_id)
    if has_applied:
        messages.error(request, 'You have already applied to this job')
        return redirect('listings')
        
    else:
        # candiate has not applied to this job before so create new job application
        # fetch the job object
        job = Job.objects.get(id=job_id)

        job_id    = job_id
        candidate = request.user
        recruiter = job.recruiter
        title     = job.title
        company   = job.company

        jobApplication = JobApplied(recruiter=recruiter, candidate=candidate, job_id=job_id,
                                    title=title, company=company)

        jobApplication.save()
        messages.success(request, 'Your application has been submitted successfully')  
        return redirect('listings')