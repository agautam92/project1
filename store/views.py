from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from user.models import CustomUser
from django.http import HttpResponse
from django.shortcuts import redirect
from store.models import Image

class Home(TemplateView):
    template_name = 'store/home.html'


class Profile(TemplateView):
    template_name = 'store/post_signup.html'

    def get(self,request, **kwargs):
        data={}
        data['user_images'] = Image.objects.filter(artist=request.user)
        return self.render_to_response(data)


class GetFilter(TemplateView):
    template_name = 'store/get_filtered.html'

    def get(self,request,*args,**kwargs):
        data = request.GET.get('program')
        return render(request,'store/get_filtered.html',context={'data':data})

class Upload(TemplateView):
    template_name = 'store/upload.html'
    def post(self,request):
        if request.method == "POST":
            image = request.FILES['artwork']
            description = request.POST['description']
            artist = request.user
            name = request.user.username
            form_data = Image(image=image,description=description,name=name,artist=artist)
            form_data.save()
            return HttpResponse("<h3>Data Stored Succesfullt </h3>")
        else:
            return HttpResponse("<h3>Something Went Wrong </h3>")