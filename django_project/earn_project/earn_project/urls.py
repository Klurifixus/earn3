"""
URL configuration for earn_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from core.views import home
from core import views
from forum.views import forum
from forum import views
from accounts import views
from django.contrib.auth.views import LoginView

 

urlpatterns = [
path('', home, name='home'),
path('forum/', views.forum, name='forum'),
path('login/', LoginView.as_view(), name='login'),
path('register/', views.register, name='register'),
path('archive/', LoginView.as_view(), name='archive'),
path('about/', LoginView.as_view(), name='about'),
path('contact/', LoginView.as_view(), name='contact'),
] 
# from django.contrib import admin
# from django.urls import path, include
# from .views import handler403, handler404, handler405, handler500

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('home.views')),
#     path('about/', include('about.views')),
#     path('contact/', include('contact.urls')),
#     path('accounts/', include('allauth.urls')),
#     path('summernote/', include('django_summernote.urls')),
# ]

# handler403 = 'movieHub.views.handler403'
# handler404 = 'movieHub.views.handler404'
# handler405 = 'movieHub.views.handler405'
# handler500 = 'movieHub.views.handler500'
