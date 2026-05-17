from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_job, name='add_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('update/<int:job_id>/', views.update_job, name='update_job'),
]