"""hello_django URL Configuration

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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('soma/<int:valor1>/<int:valor2>/', views.somas),
    path('sub/<int:valor1>/<int:valor2>/', views.subtracao),
    path('div/<int:valor1>/<int:valor2>/',  views.divi),
    path('mult/<int:valor1>/<int:valor2>/', views.multi),
    path('mari',views.mari)
]
