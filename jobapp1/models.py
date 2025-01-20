from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class AppliedJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job.title} - {self.jobseeker.username}"
