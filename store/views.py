from django.shortcuts import render
from django.views.generic import TemplateView
from user.models import CustomUser
from django.http import HttpResponse
from django.shortcuts import redirect

class Home(TemplateView):
    template_name = 'store/home.html'


class SignUPView(TemplateView):
    template_name = 'store/signup.html'

    def post(self,request,*args,**kwargs):
        if request.method =='POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if username and email:
                print("username",username,"password")
                user = CustomUser(username=username,email=email)
                user.set_password(password)
                user.save()
                return HttpResponse("<h3>You are registered Succesfully</h3>")
            else:
                return redirect("http://google.com")
        else:
            return redirect("store/signup.html")


class GetFilter(TemplateView):
    template_name = 'store/get_filtered.html'

    def get(self,request,*args,**kwargs):
        data = request.GET.get('program')
        return render(request,'store/get_filtered.html',context={'data':data})

