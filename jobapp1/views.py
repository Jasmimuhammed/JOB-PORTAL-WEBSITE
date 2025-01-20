from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, ProfileForm, JobApplyForm
from .models import Job, AppliedJob, Profile
from django.contrib.auth.models import User

# User Registration View
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'jobapp1/register.html', {'form': form})

# User Login View


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use .get() to avoid the error if field is missing
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard or desired page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Both username and password are required.")

    return render(request, 'jobapp1/login.html')


# User Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Profile Update View
@login_required

def update_profile(request):
    # Assuming a one-to-one relationship with the User model
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'jobapp1/update_profile.html', {'form': form})

# Job Dashboard View
@login_required
def dashboard(request):
    jobs = Job.objects.all()
    applied_jobs = AppliedJob.objects.filter(jobseeker=request.user)
    return render(request, 'jobapp1/dashboard.html', {'jobs': jobs, 'applied_jobs': applied_jobs})

# Apply for Job View
@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(id=job_id)
    AppliedJob.objects.create(job=job, jobseeker=request.user)
    messages.success(request, f"Successfully applied for {job.title}")
    return redirect('dashboard')

# View Applied Jobs
@login_required
def view_applied_jobs(request):
    applied_jobs = AppliedJob.objects.filter(jobseeker=request.user)
    return render(request, 'jobapp1/applied_jobs.html', {'applied_jobs': applied_jobs})

# Delete Applied Job
@login_required
def delete_applied_job(request, applied_job_id):
    applied_job = AppliedJob.objects.get(id=applied_job_id)
    if applied_job.jobseeker == request.user:
        applied_job.delete()
        messages.success(request, "Job application deleted!")
    return redirect('view_applied_jobs')

# Create your views here.
