from django.urls import path
from . import views

urlpatterns = [
    path('login', views.recruiter_login, name='recruiter_login'),
    path('logout', views.recruiter_logout, name='recruiter_logout'),
    path('register', views.recruiter_register, name='recruiter_register'),
    path('dashboard', views.dashboard, name="recruiter_dashboard"),
    path('candidates/<int:job_id>', views.candidates, name='applied_candidates'),
    path('job_post', views.job_post, name='job_post'),
]