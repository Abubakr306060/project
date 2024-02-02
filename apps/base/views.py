from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    title = "Geeks"
    settings = Settings.objects.latest('id')
    data = Data.objects.latest("id")
    projects = Project.objects.all()
    service = Service.objects.all()
    portfolio = Portfolio.objects.latest('id')
    return render(request, 'base/index.html', locals())



def contact(request):
    settings = Settings.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cause = request.POST.get('cause')
        message = request.POST.get('message')
        Contact.objects.create(name=name, phone=phone, email=email, cause=cause, message=message,)
        return redirect('index')
    return render(request, 'base/contact.html', locals())
