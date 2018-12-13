from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from .forms import Userlogin,issueform
from django.views.generic import View
from .models import Student, faculty
from django.http import Http404, HttpResponseRedirect, HttpResponse
import re
from django import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.urls import reverse


# Create your views here.

class login_form(View):
    form_class = Userlogin
    template_name = "home/login_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                id = str(request.user.id)
                return redirect('/home/'+id+'/' )
            else:
                return render(request, 'home/login_form.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login_form.html', {'error_message': 'Invalid login'})


def logout_user(request):
    logout(request)
    form = Userlogin(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'home/logout.html', context)



def index(request,id):

    user=User.objects.get(username=request.user)

    p = re.match(r'1bm[0-9]{2}[a-z]{2}[0-9]{3}@bmsce.ac.in', user.username)
    if p:
        return render(request, 'home/indexstudent.html', {'user': user, })
    f = re.match(r'^[a-z]{3}.*@bmsce.ac.in$', user.username)
    if f:
        return render(request, 'home/indexfaculty.html', {'user': user})


def about(request):
    return render(request, 'home/about.html')


def contactus(request):
    return render(request, 'home/contactus.html')


def department(request):
    return render(request, 'home/department.html')


def loginabout(request, id):
    if not request.user.is_authenticated:
        return render(request, 'home/login_form.html')
    return render(request, 'home/loginabout.html', )

@login_required
def logincontactus(request, id):
    if not request.user.is_authenticated:
        return render(request, 'home/login_form.html')
    return render(request, 'home/logincontactus.html')

@login_required
def loginhome(request, id):
    if not request.user.is_authenticated:
        return render(request, 'home/login_form.html')
    return render(request, 'home/indexstudent.html')


class studentissue(CreateView):
    model = Student
    fields = ['issue', 'usn', 'branch', 'sem']


def request(request, id):
    if not request.user.is_authenticated:
        return render(request, 'home/login_form.html')
    return render(request, 'home/facultyrequisitions.html')


class issue(forms.ModelForm):
    model = Student
    issue = forms.CharField(max_length=100)


class applied(forms.ModelForm):
    model = issue
    iss = forms.Textarea()


def lol(request):
    form1 = issue()
    form2 = applied()
    return render(request, 'home/indexfaculty.html', {'forms': [form1, form2]})


def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = resolve_url()

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous(),
        login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


"""def applyissue(request):
    if request.user.is_authenticated():
        return render(request,'home/login_form.html')
    else:
        form = issue(request.POST or None)
        if form.is_valid():
            isue=form.save(commit=False)
            isue.studentid=request.user
            student=request.user.student_set.all()
            isue.name=student.name
            isue.branch=student.branch
            #isue.sem=student.sem
            isue.facid=student.facid
            isue.issue=request.POST['issue']
            isue.subject=request.POST['subject']
            isue.save()
            return render(request,'home/studntappy.html',{'isue':isue})
        else:
            return render(request,'home/indexstudent.html',{'form':form})"""

"""def apply(request):
    object=
    if request.user is not None:
        if request.method=='POST' :
            name=request.POST['name']
            usn=request.POST['usn']
            sem=request.POST['sem']
            branch=request.POST['branch']
            subject=request.POST['subject']
            issue=request.POST['issue']
            object.name"""




class issueCreate(UpdateView):
    template = 'home/studentapply.html'
    form_class=issueform

    def get(self, request, *args, **kwargs):
        context = {}
        form = self.form_class(None)
        context['form'] = form
        return render(request,'home/studentapply.html',context)

    def post(self, request,id, **kwargs):
        form = issueform(request.POST or None)
        if form.is_valid():
            p=User.objects.get(pk=id)
            f=form.save(commit=False)
            f.user=p
            #p=form.save(commit=False)
            #p.user=request.user
            f.issue=form.cleaned_data['issue']
            f.subject=form.cleaned_data['subject']

            f.save(update_fields=['issue','subject'])


        else:
            context = {}
            form = issueform()
            context['form'] = form
            render(request,'home/studentapply.html',context)
        return redirect('/home/'+str(request.user.id)+'/apply/')






