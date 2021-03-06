from django.shortcuts import render, get_object_or_404
from .forms import userloginfrm, usersignupfrm, addform, contactform
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Student
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url=('/'))
def home(request):
    ff = Student.objects.all()
    return render(request,'app/home.html',{'fm':ff})

def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            fm = userloginfrm(request.POST)
            if fm.is_valid():
                a = fm.cleaned_data['username']
                b = fm.cleaned_data['password']
                user = auth.authenticate(username=a, password=b)
                if user is not None:
                    auth.login(request, user)
                    messages.info(request, 'You are logged In Successfully..!!')
                    return HttpResponseRedirect('/home/')
                else:
                    messages.info(request, 'Invalid credential')
        else:
            fm = userloginfrm()
        return render(request, 'app/login.html', {'fm': fm})

def usersignup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            fm = usersignupfrm(request.POST)
            if fm.is_valid():
                a = fm.cleaned_data['username']
                b = fm.cleaned_data['first_name']
                c = fm.cleaned_data['last_name']
                d = fm.cleaned_data['email']
                e = fm.cleaned_data['password']
                g = fm.cleaned_data['password2']
                if e == g:
                    f = User.objects.create_user(username=a, first_name=b, last_name=c, email=d, password=e)
                    f.save()
                    messages.success(request, 'You are Successfully Registered..!!')
                    return HttpResponseRedirect('/')
                else:
                    messages.warning(request, 'Password not matched')
        else:
            fm = usersignupfrm()
        return render(request, 'app/signup.html', {'fm': fm})


@login_required(login_url=('/'))
def userlogout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return HttpResponseRedirect('/')

    
def addstudent(request):
    if request.method == 'POST':
        ff = addform(request.POST)
        if ff.is_valid():
            ff.save()
            return HttpResponseRedirect('/home/')
    else:
        ff = addform()
    return render(request,'app/add.html',{'fm':ff})

def updatestudent(request, id):
    if request.method == 'POST':
        doc = get_object_or_404(Student, id=id)
        ff = addform(data=request.POST, instance=doc)
        if ff.is_valid():
            ff.save()
            return HttpResponseRedirect('/home/')
    else:
        doc = get_object_or_404(Student, id=id)
        ff = addform(instance=doc)
    return render(request, 'app/update.html',{'fm':ff})

def deletestudent(request, id):
    ff = get_object_or_404(Student, id=id)
    ff.delete()
    return HttpResponseRedirect('/home/')

def searchstudent(request):
    hh = request.POST['name']
    hb = Student.objects.filter(name__icontains=hh)
    return render(request, 'app/home.html', {'fm':hb})


def contact(request):
    if request.method=='POST':
        fm = contactform(request.POST)
        if fm.is_valid:
            a = request.POST['name']
            b = request.POST['email']
            c = request.POST['message']
            d = b+c
            print(b)
            print(c)
            print(b+c)
            send_mail(a,                   #for heading
             d,                            #for msg
             b, 
             ['vkd2695@gmail.com'],        #to
            )
            return HttpResponseRedirect('/home/')
    else:
        fm = contactform()
    return render(request, 'app/help.html',{'fm':fm})
