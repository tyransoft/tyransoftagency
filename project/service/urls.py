from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name=''),
    path('about',views.about,name='about'),
    path('add_service',views.add_service,name='add_service'),
    path('service/<int:pk>',views.service_desc,name='service'),
    path('add_customer',views.add_customer,name='add_customer'),


]