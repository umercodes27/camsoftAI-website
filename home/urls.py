from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('service', views.service, name='service'),
    path('features', views.features, name='features'),
    path('price', views.price, name='price'),
    path('quote', views.quote, name='quote'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('tinymce/', include('tinymce.urls')),

]