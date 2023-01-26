import os

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def subpage(request):
    return render(request,"subpage.html")

def userregister(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            un=a.cleaned_data['uname']
            ph=a.cleaned_data['phno']
            em=a.cleaned_data['email']
            psw=a.cleaned_data['passw']
            cpsw=a.cleaned_data['cpassw']
            place=a.cleaned_data['place']
            ut=a.cleaned_data['utype']
            if psw==cpsw:
                b=regmodel(fname=fn,uname=un,phno=ph,email=em,passw=psw,place=place,utype=ut)
                b.save()
                return redirect(ulogin)
            else:
                return HttpResponse("password doesn't match")
        else:
            return HttpResponse('registration failed')

    return render(request,'userreg.html')

def ulogin(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            uname=a.cleaned_data['uname']
            psw=a.cleaned_data['psw']
            b=regmodel.objects.all()
            for i in b:
                if uname==i.uname and psw==i.passw:
                    email=i.email
                    return render(request,'userhome.html',{'uname':uname,'email':email})
            else:
                    return HttpResponse('login failed')

    else:
        return render(request,'userlogin.html')


def storeregister(request):
    if request.method=='POST':
        a=storeregform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['username']
            em=a.cleaned_data['email']
            psw=a.cleaned_data['password']
            b=storemodel(username=un,email=em,password=psw)
            b.save()
            return redirect(storelogin)

        else:
            return HttpResponse('registration failed')

    return render(request,'register.html')

def storelogin(request):
    if request.method=='POST':
        a=storelogform(request.POST)
        if a.is_valid():
            uname=a.cleaned_data['username']
            psw=a.cleaned_data['password']
            b=storemodel.objects.all()
            for i in b:
                if uname==i.username and psw==i.password:
                    email=i.email
                    return render(request,'storehome.html',{'username':uname,'email':email})
            else:
                    return HttpResponse('login failed')

    else:
        return render(request,'storelogin.html')



def userhome(request):
    return render(request,'userhome.html')

def userheader(request):
    return render(request,'userheader.html')

def storeheader(request):
    return render(request,'storeheader.html')


def header(request):
    return render(request,'header.html')

def footer(request):
    return render(request,'footer.html')

def storehome(request):
    return render(request,'storehome.html')

def book(request):
    if request.method=="POST":
        a=bookform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['bname']
            pr=a.cleaned_data['bprice']
            des=a.cleaned_data['des']
            img=a.cleaned_data['image']
            b=bookmodel(bname=nm,bprice=pr,des=des,image=img)
            b.save()

            return redirect(bookdisplay)
        else:
            return HttpResponse('upload failed')
    else:
        return render(request,'addbooks.html')

def bookdisplay(request):
    a=bookmodel.objects.all()
    li=[]
    name=[]
    dis=[]
    price=[]
    id=[]
    for i in a:
        id1=i.id
        id.append(id1)
        path=i.image
        li.append(str(path).split("/")[-1])
        nm=i.bname
        name.append(nm)
        dis1=i.des
        dis.append(dis1)
        pr=i.bprice
        price.append(pr)
    mylist=zip(li,name,dis,price,id)

    return render(request,'bookdisplay.html',{'mylist':mylist})


def editbook(request,id):
    prod=bookmodel.objects.get(id=id)
    a=str(prod.image).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image=request.FILES['image']
        prod.bname=request.POST.get('bname')
        prod.des = request.POST.get('des')
        prod.bprice = request.POST.get('bprice')
        prod.save()
        return redirect(bookdisplay)
    context={'prod':prod,'a':a}

    return render(request,'editbook.html',context)

def deletebook(request,id):
    prod=bookmodel.objects.get(id=id)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    return redirect(bookdisplay)


def viewbook(request):
    a=bookmodel.objects.all()
    li=[]
    name=[]
    dis=[]
    price=[]
    id=[]
    for i in a:
        id1=i.id
        id.append(id1)
        path=i.image
        li.append(str(path).split("/")[-1])
        nm=i.bname
        name.append(nm)
        dis1=i.des
        dis.append(dis1)
        pr=i.bprice
        price.append(pr)
    mylist=zip(li,name,dis,price,id)

    return render(request,'viewbook.html',{'mylist':mylist})

def addcontact(request):
    if request.method=="POST":
        a=profileform(request.POST,request.FILES)
        if a.is_valid():
            cid = a.cleaned_data['cid']
            name = a.cleaned_data['name']
            loc = a.cleaned_data['loc']
            phn=a.cleaned_data['phn']
            b=profilemodel(cid=cid,name=name,loc=loc,phn=phn)
            b.save()

            return HttpResponse('success')
        else:
            return HttpResponse('failed')
    else:
        return render(request,'addcontact.html')


def contactdisplay(request):
        a = profilemodel.objects.all()
        name = []
        loc = []
        phn = []
        cid = []
        id=[]
        for i in a:
            id1 = i.id
            id.append(id1)
            cid1 = i.cid
            cid.append(cid1)
            nm=i.name
            name.append(nm)
            loc1=i.loc
            loc.append(loc1)
            pn = i.phn
            phn.append(pn)
        mylist = zip( cid,name, phn,loc,id)

        return render(request, 'contactdisplay.html', {'mylist': mylist})



def editprofile(request,id):
    prod=profilemodel.objects.get(id=id)
    if request.method == 'POST':
        prod.name=request.POST.get('name')
        prod.cid = request.POST.get('cid')
        prod.loc = request.POST.get('loc')
        prod.phn = request.POST.get('phn')
        prod.save()
        return redirect(contactdisplay)
    context={'prod':prod}

    return render(request,'editprofile.html',context)


def addtocart(request,id):
    a=bookmodel.objects.get(id=id)
    b=addcart(bookname=a.bname,bookprice=a.bprice,bookimage=a.image)
    b.save()
    return redirect(cartdisplay)


def cartdisplay(request):
    a = addcart.objects.all()
    li=[]
    name = []
    price = []

    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        path = i.bookimage
        li.append(str(path).split("/")[-1])
        price1 = i.bookprice
        price.append(price1)
        nm = i.bookname
        name.append(nm)


    mylist = zip(li, name, price,  id)

    return render(request, 'cartdisplay.html', {'mylist': mylist})

def removecart(request,id):
    prod=addcart.objects.get(id=id)
    if len(prod.bookimage) > 0:
        os.remove(prod.bookimage.path)
    prod.delete()
    return redirect(cartdisplay)

def buynow(request,id):
   a=addcart.objects.get(id=id)
   if request.method=='POST':
        amount=int(request.POST.get('bprice'))
        qua=int(request.POST.get('quantity'))
        total=amount*qua
        return render(request,'bill.html',{'total':total})

   return render(request,'buynow.html',{'a':a})

    # prod=bookmodel.objects.get(id=id)
    # a = str(prod.image).split('/')[-1]
    # if request.method == 'POST':
    #     if len(request.FILES) != 0:
    #         prod.image=request.FILES['image']
    #     prod.bname=request.POST.get('bname')
    #     prod.bprice=request.POST.get('bprice')
    #
    #     quantity=request.POST('quantity')
    #     if request.method=='POST':
    #         bookname=request.POST.get('bname')
    #         bookprice = request.POST.get('bprice')
    #         quantity = request.POST.get('quantity')
    #         amount=quantity*bookprice
    #         return render(request,"total.html",amount)
    #     return render(request,'buynow.html')

def bill(request):
    return render(request,'bill.html')

def payment(request):
    return render(request,'payment.html')