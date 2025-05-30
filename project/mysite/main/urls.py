"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name="login"),         # Login page as homepag
    path('home/', views.home, name="home"),   # After login, redirect here
    path('about/', views.about, name="about"),
    path('complain/',views.complain, name="complain"),
    path('mycomplain/',views.my_complain, name="my_complain"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
]

