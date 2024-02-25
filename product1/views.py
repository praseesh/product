from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, "addlist.html")

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

def display (request):
    product_list = Product.objects.all()
    return render(request, 'addlist.html', {'pdt':product_list})

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
    
def delete(request):
    if request.method == 'POST':
        cmpname = request.POST.get('company','')
        cmpdtls = Product.objects.filter(company = cmpname)
        if cmpdtls.exists():
            cmpdtls.delete()
            return render(request, 'addlist.html', {"msg": "Deleted"})
        else:
            return render(request, 'addlist.html', {"msg": "NO RECORDS FOUND!"})
