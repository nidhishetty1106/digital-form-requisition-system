from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.login_form.as_view()),
    re_path(r'^(?P<id>.+)/$',views.index)
]
