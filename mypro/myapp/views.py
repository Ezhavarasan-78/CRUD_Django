from django.shortcuts import render,redirect
from .models import FORM


def home(request):
    return render(request,'index.html')

 


def add(request):
    info=FORM.objects.all()
    return render(request,'record.html',{'info':info})

def addrec(request):
    a=request.POST.get('user')
    b=request.POST.get('reg_no')
    c=request.POST.get('dept')
    d=request.POST.get('email')
    
    info=FORM(name=a,reg_no=b,Dept=c,email=d)
    info.save();
    return redirect('add')

def delete(request, id):
    info=FORM.objects.get(id=id)
    info.delete();
    return redirect('add')

def update(request,id):
    info=FORM.objects.get(id=id)
    return render(request,'update.html',{'info':info})

    
def uprec(request,id):
    a=request.POST.get('user')
    b=request.POST.get('reg_no')
    c=request.POST.get('dept')
    d=request.POST.get('email')
    
    info=FORM.objects.get(id=id)
    info.name=a
    info.reg_no=b
    info.Dept=c
    info.email=d
    info.save();
    return redirect('add')
    