from django.shortcuts import render
from .models import Talaba  
# Create your views here.

def Talaba_function(request):
    stu = Talaba.objects.all()
    return render(request, 'index.html', {"stu":stu})