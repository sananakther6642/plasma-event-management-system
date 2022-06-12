"""plasmaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from plasmaapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    
    path('',index),
    path('regfor/',regfor),
    path('que/',que),
    path('query/',query),
    
    
    
    path('reg/',reg),
    path('pay/',pay),
    path('paydetails/',paydetails),
    path('dashboard/',dashboard),
    path('regdata/',regdata),
    path('regdetails/',regdetails),
    path('export_users_xls/',export_users_xls,name='export_excel'),
    path('export_excel2/',export_excel2,name='export_excel2'),
    path('export_excel3/',export_excel3,name='export_excel3'),
    
    
    
    
    
    path('regval/',regval),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
