from django.shortcuts import render,redirect
from django.http import HttpResponse
#from blog.forms import BlogForm as BF
from django.contrib.auth import authenticate as aut
from django.contrib.auth.models import User
#from leave_mngt.models import shift_rota as sr
from django.contrib import messages,auth
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    valuenext = request.GET.get('next','/')
    print(valuenext)
    if request.user.is_authenticated:
        return redirect('home')
    context = {
        'title': 'Login',
        'valuenext': valuenext,
    }
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=aut(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            #page_object=sr.objects.all()
            return redirect(valuenext)
            #return redirect('home')
            #return render(request,'leave_mngt/homepage.html',{})
        else:
            return render(request,"leave_mngt/login.html",{})
    else:
        return render(request,'leave_mngt/login.html',context)

def signout_view(request):
    auth.logout(request)
    return redirect("/")

# def signout_view(request):
#     try:
#         del request.session['member_id']
#     except KeyError:
#         pass
#     return HttpResponse("You're logged out")

def signup_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return render(request,'leave_mngt/signup.html',{})
            else:
                user=User.objects.create(username=username,password=password1)
                user.save()
                messages.info(request,"User Created Successfully")
                return redirect("/")
        else:
            messages.info(request,"Password doesn't match")
            return render(request,'leave_mngt/signup.html',{})
    else:
        return render(request,'leave_mngt/signup.html',{})
