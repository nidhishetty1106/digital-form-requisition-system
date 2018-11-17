from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import Userlogin
from django.views.generic import View
from django.http import Http404
import re
# Create your views here.

class login_form(View):
    form_class=Userlogin
    template_name = "home/login_form.html"
    def get(self, request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    id=str(request.user.id)
                    return redirect('/home/'+id+'/')
                else:
                    return render(request, 'home/login_form.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'home/login_form.html', {'error_message': 'Invalid login'})


def index(request,id):
    try:
        user= User.objects.get(pk=id)

    except User.DoesNotExist:
        raise Http404('User does not exist')

    p=re.match(r'1bm[0-9]{2}[a-z]{2}[0-9]{3}@bmsce.ac.in',user.username)
    if p:
        return render(request, 'home/indexstudent.html', {'user': user})
    f=re.match(r'^[a-z]{3}.*@bmsce.ac.in$',user.username)
    if f:
        return render(request, 'home/indexfaculty.html', {'user': user})








