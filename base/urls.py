# my_project/urls.py
from django.shortcuts import render
from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('service/', views.service, name='service'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/', views.blog, name='blog'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.teams, name='teams'),
    path('team/', views.team, name='team'),
]

# This view will handle 404 errors
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

# Assign the custom_404_view to handle 404 errors
handler404 = custom_404_view
