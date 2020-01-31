from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from jobs.models import Job, JobApplied

def index(request):
    """View for home page"""
    return render(request, 'pages/index.html')

def login(request):
    """View for candidate login """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'pages/login.html')

def logout(request):
    """View for candidate logout """
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

def register(request):
    """View for candidate register """
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
        # Check username
            if User.objects.filter(username=username).exists():
                # the username already exists
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    # the email used already exists
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            # error if passwords didnot match
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'pages/register.html')

def listings(request):
    """View for job listings"""

    jobs = Job.objects.order_by('-upload_date')
    paginator = Paginator(jobs, 3)
    page = request.GET.get('page')
    paged_jobs = paginator.get_page(page)

    context = {
        'jobs' : paged_jobs
    }

    return render(request, 'pages/listings.html', context)

def dashboard(request):
    """View for candidate dashboard"""

    # fetch all the job the user has applied to
    applications = JobApplied.objects.filter(candidate=request.user)

    context = {
        'applications' : applications
    }

    return render(request, 'pages/dashboard.html', context)