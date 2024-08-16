from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required
def home(request):
    return render(request, "addlist.html")

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username = uname, password = pwd)
    if user is not None:
        login(request,user)
        return redirect('home')
    else :
        return render(request,"login.html",{"msg": "You are an Unauthorized person"})

def logoutview(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    form = UserCreationForm(request.POST)
    try:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('login')
            return render (request, 'sign_up.html', {'form':userform, 'msg':'Invalid login'})
        else:
            return render (request, 'sign_up.html', {'form':userform, 'msg':'Invalid submission'})
    except Exception as e:
        print(e)
        userform = UserCreationForm()
        return render(request, 'sign_up.html', {'form': userform})

def Resethome(request):
    return render(request,'ResetPassword.html')

def resetPassword(request):
    uname = request.POST['uname']
    newpwd = request.POST ['password']

    try:
        user = User.objects.get(username = uname)
        if user is not None:
            user.set_password(newpwd)
            user.save()
            return render(request,'ResetPassword.html',{'msg':'password Reset Successfully'})
    except Exception as e:
        print (e)
        return render(request,"ResetPassword.html", {'msg':'Password Reset Failed'})
    

@login_required
def add(request):
    try:
        Company = request.POST['company']
        Description = request.POST['description'] 
        Price = int(request.POST['price'])
        Stock = int(request.POST['stock'])

        probj = Product.objects.create(
            company=Company,
            description=Description,
            price=Price,
            stock=Stock)
        probj.save()
        return render(request,'addlist.html', {"msg":"Product Added"})
    
    except Exception as e:
        print (e)
        return render(request,'addlist.html',{"msg":"Product Can't be Added"})
    
@login_required
def display (request):
    product_list = Product.objects.all()
    return render(request, 'addlist.html', {'pdt':product_list})

@login_required
def update (request):
    try:
        oldcompanyname = request.POST['oldcompanyname']
        newcompanyname = request.POST["newcompanyname"]
        pdt = Product.objects.filter(company=oldcompanyname)
        if pdt.exists():
            pdt.update(company=newcompanyname)
            return render(request, 'addlist.html',{'msg1':'Company name Updated'})
        else:
            return render(request, 'addlist.html',{'msg1':'No Records Found'})
        
    except Exception as e:
        print(e)
        return render(request,"addlist.html",{'msg1':"Not Updated"})
    
@login_required
def delete(request):
    if request.method == 'POST':
        cmpname = request.POST.get('company','')
        cmpdtls = Product.objects.filter(company = cmpname)
        if cmpdtls.exists():
            cmpdtls.delete()
            return render(request, 'addlist.html', {"msg": "Deleted"})
        else:
            return render(request, 'addlist.html', {"msg": "NO RECORDS FOUND!"})
