from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('applied_jobs/', views.view_applied_jobs, name='view_applied_jobs'),
    path('delete_applied_job/<int:applied_job_id>/', views.delete_applied_job, name='delete_applied_job'),
]
