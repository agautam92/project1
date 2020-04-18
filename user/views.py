from django.shortcuts import render

from store.models import Image
from .models import CustomUser
from django.views.generic import TemplateView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.shortcuts import redirect


class SignUPView(TemplateView):
    template_name = 'store/home.html'

    def post(self,request,*args,**kwargs):
        if request.method =='POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if username and email:
                user = CustomUser(username=username,email=email)
                user.set_password(password)
                user.save()
                return render(request,'store/post_signup.html',context={'username':username})
            else:
                return HttpResponse("<h3>You are NOT registered </h3>")
        else:
            return redirect("store/signup.html")


class LoginView(TemplateView):
    template_name = 'store/home.html'

    def post(self,request,*args,**kwargs):
        if request.method =='POST':
            parameters = request.POST
            username = parameters.get('username')
            password = parameters.get('password')
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return render(request,'store/home.html')
            else:
                return HttpResponse("Invalid credentials")


def logout_user(request):
    logout(request)
    return render(request,'store/home.html',context={'username':None})