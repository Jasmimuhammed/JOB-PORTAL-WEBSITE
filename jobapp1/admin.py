from django.contrib import admin
from .models import Job, Profile, AppliedJob

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_date')
    search_fields = ('title', 'company', 'location')
    list_filter = ('posted_date', 'location')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'phone_number', 'location')
    search_fields = ('user__username', 'bio', 'phone_number', 'location')

class AppliedJobAdmin(admin.ModelAdmin):
    list_display = ('job', 'jobseeker', 'applied_on')
    list_filter = ('applied_on', 'job')
    search_fields = ('job__title', 'jobseeker__username')

# Register the models with the admin site
admin.site.register(Job, JobAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AppliedJob, AppliedJobAdmin)


# Register your models here.
