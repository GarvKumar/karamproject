from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('products/', views.products, name="products"),
    path('services/', views.services, name="services"),
    path('videos/', views.videos, name="videos"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    path('contact/enquiry', views.enquiry, name="enquiry"),
    path('contact/complaint', views.complaint, name="complaint"),
    path('contact/feedback', views.feedback, name="feedback"),
    path('replytoclient/', views.replytoclient, name="replytoclient"),
]
