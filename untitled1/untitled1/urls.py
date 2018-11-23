
from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('',include('home.urls'))
]
