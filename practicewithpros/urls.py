"""practicewithpros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

#from cuser.forms import AuthenticationForm
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib import admin
from django.urls import path #, include#, URLPattern
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #need to get login to forward if already logged in...
    
#     url(r'^accounts/login/$', LoginView.as_view(authentication_form=AuthenticationForm), name='login'),
#     url(r'^accounts/logged_out/$', LogoutView.as_view(template_name = 'registration/logged_out.html'), name='logged_out'),
#     url(r'^accounts/', include('django.contrib.auth.urls')),
    
    #path(r'', include('django.contrib.auth.urls')),
        
    path('admin/', admin.site.urls),
    
    #url(r'^redirect/$', redirect_view, name='url_to_redirect_to'),
    
    path('', include('home.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)