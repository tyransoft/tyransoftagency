from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import myinfo
# Create your views here.
def contact_us(request):
    info=myinfo.objects.first()
    if request.method == 'POST': 
     email=request.POST.get('Email')
     subject=request.POST.get('Subject')
     message=request.POST.get('Message')
     send_mail(
        subject,
        message,
        email,
        [settings.EMAIL_HOST_USER]
     )
     return redirect("/")
    return render(request,'contact/contact.html',{'myinfo':info})
