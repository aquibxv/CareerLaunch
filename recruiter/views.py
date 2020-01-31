from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from jobs.models import Job

# Create your views here.
def recruiter_login(request):
    """View for recruiter login"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('recruiter_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('recruiter_login')
    else:
        return render(request, 'recruiter/recruiter_login.html')

def recruiter_logout(request):
    """View for recruiter logout"""
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def recruiter_register(request):
    """view for recruiter register"""
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
                return redirect('recruiter_register')
            else:
                if User.objects.filter(email=email).exists():
                    # the email used already exists
                    messages.error(request, 'That email is being used')
                    return redirect('recruiter_register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('recruiter_login')

        else:
            # error if passwords didnot match
            messages.error(request, 'Passwords do not match')
            return redirect('recruiter_register')
    
    else:
        return render(request, 'recruiter/recruiter_register.html')

def dashboard(request):
    """view for recruiter dashboard"""

    jobs = Job.objects.order_by('-upload_date')
    jobs = jobs.filter(recruiter = request.user)

    context = {
        'jobs' : jobs
    }

    return render(request, 'recruiter/dashboard.html', context)

def job_post(request):
    """View for posting a job"""
    if request.method == 'POST':

        #Get form value
        recruiter = request.user
        title = request.POST.get('job_title')
        company = request.POST.get('company-name')
        salary = request.POST.get('salary')
        location = request.POST.get('location')
        description = request.POST.get('job-descript')

        job = Job.objects.create(recruiter=recruiter, title=title, company=company, salary=salary,
                                location=location, description=description)

        messages.success(request, "Job has been posted successfully")
        return redirect('recruiter_dashboard')

    else:
        return render(request, 'recruiter/job_post.html')
    