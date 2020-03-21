"""ssosite URL Configuration
 
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include#, URLPattern
#from SSO.views import clients
from django.conf.urls.static import static
import home.views as sviews
 
 
urlpatterns = [
    path('', sviews.home, name='home'),
    path('home/', sviews.home, name='home'),  
    
    
#     path('catalog/', sviews.catalogbug, name='home'),  
#     path('staff/', sviews.admin_home, name='staff-home'),   
#     path('register/<slug:regkey>/', sviews.registration, name='finish-registration'), 
#     path('staff/lists/', sviews.admin_lists, name='staff-lists'),   
#     path('staff/config/', sviews.admin_home, name='staff-admin-home'),
#     path('SSO/<int:target>/', sviews.sso_out, name='SSO'),
    
]
