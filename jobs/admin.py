from django.contrib import admin
from .models import Job, JobApplied

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'recruiter', 'upload_date']
    list_display_links = ['title', 'company']
    list_filter = ['title', 'company', 'recruiter', 'upload_date']

admin.site.register(Job, JobAdmin)

class JobAppliedAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'candidate', 'recruiter', 'applied_date']
    list_display_links = ['title', 'company']
    list_filter = ['title', 'company', 'recruiter', 'applied_date']

admin.site.register(JobApplied, JobAppliedAdmin)