from django.shortcuts import render,redirect
from . models import *

# Create your views here.
def homepage(request):
    return render(request,'index.html')


def student(request):
    if request.method =='POST':
        name=request.POST.get('name')
        roll_number=request.POST.get('roll_number')
        Email=request.POST.get('Email')
        models.student.object.create(name=name,roll_number=roll_number,Email=Email)
        return redirect('student')
    students=student.object.all()
    return render(request,'idex.html'),{'student':student}



