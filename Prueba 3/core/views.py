from core.forms import formAgregar
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout  
from django.shortcuts import redirect, render
from .models import Producto
from django.contrib.auth.models import User



# Create your views here.

def home(request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'home.html',contexto)

def Admin(request):
    producto = Producto.objects.all()
    datos = {
        'producto':producto,
        'form' : formAgregar()
    }
    if request.method=='POST':
        formulario = formAgregar(request.POST,request.FILES)
        if formulario.is_valid :
                formulario.save()
                datos   ['mensaje'] = "Los datos se guardaron correctamente "
                
    return render(request,'Admin.html',datos)

def MB(request):
    return render(request,'MB.html',{})

def CPU(request):
    return render(request,'CPU.html',{})

def GPU(request):
    return render(request,'GPU.html',{})

def HDD(request):
    return render(request,'HDD.html',{})

def M2(request):
    return render(request,'M2.html',{})

def PSU(request):
    return render(request,'PSU.html',{})

def RAM(request):
    return render(request,'RAM.html',{})

def SSD(request):
    return render(request,'SSD.html',{})
def Signin(request):
    contexto = {}
    return render(request,'Signin.html',{})

def Logeando (request):
    username = request.POST.get('Usuario','')
    password = request.POST.get('password','')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('Signin')

def Deslogeo (request): 
    logout(request)
    return redirect('home')


def Registrando(request): 
    usuario = request.POST.get('usuario','') 
    password = request.POST.get('password2','')
    email = request.POST.get('Email','')
    user = User.objects.create_user(usuario,email,password)
    user.save()
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('Signin')

def Signup (request):
    return render(request,'Signup.html',{})



    



