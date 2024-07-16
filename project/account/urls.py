from django.urls import path
from . import views
urlpatterns=[
    path('user_singup',views.user_singup,name='user_singup'),
    path('user_logout',views.user_logout,name='user_logout'),

]