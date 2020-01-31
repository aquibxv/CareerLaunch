from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')), 
    path('recruiter/', include('recruiter.urls')),
    path('application/', include('jobs.urls')),
    path('admin/', admin.site.urls)
]