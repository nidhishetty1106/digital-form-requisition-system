from django.urls import path, re_path
from django.conf.urls import url
from . import views
import re
from django.contrib.auth.decorators import login_required
app_name = 'home'
urlpatterns = [
    path('', views.login_form.as_view(), name='home'),
    #path('loginuser/', views.index, name='login'),
    re_path(r'^(?P<id>[0-9]+)/$', login_required(views.index), name='id'),
    re_path(r'^(?P<id>[0-9]+)/apply/$', views.issueCreate.as_view(), name='issuecreate'),
    # re_path(r'^(?P<id>.+)/logout_user/$', views.logout_user, name='logout_user'
    path('about', views.about, name='about'),
    path('contactus', views.contactus),
    path('department', views.department),
    # path('loginuser/apply',views.issueCreate.as_view()),
    re_path(r'^(?P<id>[0-9]+)/about$', views.loginabout, name='loginabout'),
    re_path(r'^(?P<id>[0-9]+)/contactus$', views.logincontactus, name='contactus'),
    path('logout',views.logout_user,name='logout')

]
