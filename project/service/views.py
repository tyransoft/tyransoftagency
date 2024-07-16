from django.shortcuts import render,redirect
from .models import service,customer
from .forms import servicefrom,customerfrom
# Create your views here.
def home(request):    
    Service=service.objects.all()
    Customer=customer.objects.all()
    context={'service':Service,'customers':Customer}
    return render(request,'project/index.html',context)
def service_desc(request, pk):
    service_desc=service.objects.get(pk=pk)
    return render(request,'project/service_desc.html',{'service':service_desc})



def about(request):
    return render(request,'project/about.html')
def add_service(request):
    Add_Service=service.objects.all()
    if request.method == "POST":
      form=servicefrom(request.POST,request.FILES)
      if form.is_valid:
        form.save()
        return redirect('/')
    else:
      form=servicefrom()     
    return render(request,'project/add_service.html',{'form':form})   
def add_customer(request):
    if request.method == "POST":
      form=customerfrom(request.POST,request.FILES)
      if form.is_valid:
        form.save()
        return redirect('/')
    else:
      form=customerfrom()     
    return render(request,'project/add_customer.html',{"form":form})   
