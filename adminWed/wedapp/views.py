from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from wedapp.models import user,hallbook,add,msg
now=datetime.now()
# Create your views here.

def login(request):

    return render(request, 'login.html', {})

def log(request):
    if request.method == 'POST':
        email = request.POST['mail']
        pwd = request.POST['pass']

        if email=="karna@gmail.com" and pwd=="karna":
            return HttpResponseRedirect('/front')

        elif user.objects.filter(Mail=email).exists():
            request.session['user']=email
            return HttpResponseRedirect('/')

        elif add.objects.filter(Mail=email).exists():
            request.session['user']=email
            return HttpResponseRedirect('/detail')

        else:
            return HttpResponseRedirect('/register')


def logout(request):
    del request.session['user']
    return render(request,'login.html')

def register(request):
    return render(request, 'register.html', {})

def reg(request):
    if request.method == 'POST':
        frist = request.POST['fname']
        last = request.POST['lname']
        email = request.POST['mail']
        pwd = request.POST['pass']
        pwd1 = request.POST['pass1']

        if user.objects.filter(Mail=email).exists():
            return HttpResponseRedirect('/login')

        elif pwd==pwd1:
            saverecord=user()
            saverecord.Firstname=frist
            saverecord.Lastname=last
            saverecord.Mail=email
            saverecord.Password=pwd
            saverecord.save()
            messages.success(request,'Registion Successfully')
            return HttpResponseRedirect('/login')

        else:
            return render(request,'register.html')


def forgot(request):
    return render(request, 'forgot-password.html', {})

def got(request):
    if request.method == 'POST':
        email = request.POST['mail']

        if user.objects.filter(Mail=email).exists():
            word = request.POST['pass']

            saverecord=user.objects.get(Mail=email)
            saverecord.Password=word
            saverecord.save()
            messages.success(request,'Password Changed')
            return HttpResponseRedirect('/login')
        else:
            
            return HttpResponseRedirect('/register')

def dash(request):
    res=msg.objects.all()
    return render(request,'dashboard.html',{'view':res})

def front(request):
    return render(request, 'front.html', {})

def face(request):
    res=add.objects.filter(Id=id)
    return render(request,'home.html',{'view':res})

def home(request):
    res=add.objects.all()
    return render(request,'home.html',{'view':res})

def viewdate(request):
    return render(request,'book.html',{})

def reserve(request,id):
    if request.session.has_key('user'):
        email=request.session['user'] 
        res=add.objects.get(Id=id)
        book=hallbook.objects.all()
        return render(request, 'book.html', {'view':res,'date':book,})
    else:
        return render(request, 'login.html')

def detail(request):
    return render(request, 'index.html', {})

def date(request):
    return render(request,'index.html',{})

def alter(request):
    if request.method == 'POST':
        email = request.POST['mail']
        pwd = request.POST['pass']

        if add.objects.filter(Mail=email).exists():
            request.session['user']=email
            res=add.objects.get(Mail=email)
            book=hallbook.objects.all()
            return render(request,'index.html',{'view':res,'date':book})
        else:
            return HttpResponseRedirect('/')


def view(request):
    res=add.objects.all()
    return render(request,'view.html',{'view':res})


def tablelogin(request):
    res=user.objects.all()
    return render(request, 'table-login.html', {'view':res})

def tablebook(request):
    res=hallbook.objects.all()
    return render(request, 'table-book.html', {'view':res})


def chat(request):
    res=msg.objects.all()
    return render(request, 'comment.html', {'view':res})

def order(request):
    if request.session.has_key('user'):
        un=request.session['user']
        res=hallbook.objects.filter(Mail=un)
        return render(request,'order.html',{'view':res,'name':un})
    else:
        return render(request,'login.html')

def edit(request,id):
    res=hallbook.objects.get(Id=id)
    return render(request,'edit.html',{'view':res})

def delete(request,id):
    res=hallbook.objects.get(Id=id)
    res.delete()
    return HttpResponseRedirect('/order')

def deletehall(request,id):
    res=add.objects.filter(Id=id)
    res.delete()
    return HttpResponseRedirect('/view')

def deletelogin(request,id):
    res=user.objects.filter(Id=id)
    res.delete()
    return HttpResponseRedirect('/tablelogin')

def Add(request):
    if request.method == 'POST':
        hall = request.POST['hallname']
        ress = request.POST['address']
        ma = request.POST['mail']
        ct = request.POST['cost']
        m = request.POST['map']
        pt = request.FILES['file']

        saverecord=add()
        saverecord.HallName=hall
        saverecord.Address=ress
        saverecord.Mail=ma
        saverecord.Cost=ct
        saverecord.Map=m
        saverecord.Photo=pt
        saverecord.save()
        messages.success(request,'Record Saved Successfully')
        return HttpResponseRedirect('/view')

    else:
        return render(request, 'add.html', {})


def blank(request):
    return render(request, 'blank.html', {})

def ed(request,id):
    res=add.objects.get(Id=id)
    return render(request,'blank.html',{'view':res})

def Addedit(request):
    if request.method == 'POST':
        hall = request.POST['hallname']
        ress = request.POST['address']
        ma = request.POST['mail']
        ct = request.POST['cost']
        m = request.POST['map']
        pt = request.FILES['file']

        saverecord=add.objects.get(Mail=ma)
        saverecord.HallName=hall
        saverecord.Address=ress
        saverecord.Mail=ma
        saverecord.Cost=ct
        saverecord.Map=m
        saverecord.Photo=pt
        saverecord.save()
        messages.success(request,'Record Saved Successfully')
        return HttpResponseRedirect('/view')

    else:
        return render(request, 'blank.html', {})


def hall(request):    
    if request.method == 'POST':
        hall = request.POST['wed']
        na = request.POST['user']
        ma = request.POST['mail']
        no = request.POST['mobile']
        u = request.POST['fun']
        ck = request.POST['in']
        ek = request.POST['out']

        saverecord=hallbook()
        saverecord.Hall = hall
        saverecord.Name = na
        saverecord.Mail=ma
        saverecord.Mobileno=no
        saverecord.Fun=u
        saverecord.Checkin=ck
        saverecord.Checkout=ek
        saverecord.save()
        messages.success(request,'Booking Successfully')
        return HttpResponseRedirect('/order')

def editorder(request):
    if request.method == 'POST':
        hall = request.POST['hal']
        na = request.POST['nam']
        ma = request.POST['mail']
        no = request.POST['number']
        u = request.POST['fun']
        ck = request.POST['in']
        ek = request.POST['out']

        saverecord=hallbook.objects.get(Mail=ma)
        saverecord.Hall=hall
        saverecord.Name=na
        saverecord.Mail=ma
        saverecord.Mobileno=no
        saverecord.Fun=u
        saverecord.Checkin=ck
        saverecord.Checkout=ek
        saverecord.save()
        messages.success(request,'Edited')
        return HttpResponseRedirect('/order')
    else:
        return render(request,'edit.html')

def halluse(request):    
    if request.method == 'POST':
        hall = request.POST['wed']
        na = request.POST['user']
        ma = request.POST['mail']
        no = request.POST['mobile']
        u = request.POST['fun']
        ck = request.POST['in']
        ek = request.POST['out']

        saverecord=hallbook()
        saverecord.Hall = hall
        saverecord.Name = na
        saverecord.Mail=ma
        saverecord.Mobileno=no
        saverecord.Fun=u
        saverecord.Checkin=ck
        saverecord.Checkout=ek
        saverecord.save()
        return HttpResponseRedirect('/detail')

def call(request):
    if request.method == 'POST':
        n = request.POST['name']
        m = request.POST['email']
        no = request.POST['phno']
        ment = request.POST['comment']
        
        saverecord=msg()
        saverecord.Name=n
        saverecord.Email=m
        saverecord.Mobileno=no
        saverecord.Comment=ment
        saverecord.save()
        messages.success(request,'Request Massage Send Successfully')
        return HttpResponseRedirect('/')
    else:
        return render(request,'home.html')


