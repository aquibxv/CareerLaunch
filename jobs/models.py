from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    """ Model for representing a job """

    recruiter   = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=40, blank=False)
    company     = models.CharField(max_length=40, blank=False)
    salary      = models.CharField(max_length=40, blank=False)
    location    = models.CharField(max_length=40, blank=False)
    description = models.TextField(max_length=225, blank=False)
    upload_date = models.DateField(default=datetime.now)

    def __str__(self):
        """Django uses this to convert an object to a string"""
        return self.title

class JobApplied(models.Model):
    """ Model for representing an applied job application"""

    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_job_recruiter')
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_job_applicant')
    job_id    = models.IntegerField(blank=False, default=0)
    title     = models.CharField(max_length=40)
    company   = models.CharField(max_length=40)
    applied_date = models.DateField(default=datetime.now)

    def __str__(self):
        """Django uses this to convert an object to a string"""
        return self.title