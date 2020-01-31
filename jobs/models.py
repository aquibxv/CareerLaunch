from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=False)
    company = models.CharField(max_length=40, blank=False)
    salary = models.CharField(max_length=40, blank=False)
    location = models.CharField(max_length=40, blank=False)
    description = models.TextField(max_length=225, blank=False)
    upload_date = models.DateField(default=datetime.now)

    def __str__(self):
        """Django uses this to convert an object to a string"""
        return self.title