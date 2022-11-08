"""keeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from turtle import home
from django.contrib import admin
from django.urls import path, re_path, include
from Sandbox import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
]

contact_patterns = [
    
    path("", views.vlozh),
    path('work', views.work),
    path('workplace', views.workplace)
] # сгруппированные маршруты для вложения

urlpatterns = [
    path('info', TemplateView.as_view(template_name = "info.html", extra_context={"inject": "кал калыч"})), #представление напрямую из шаблона (templates)
    
    path('set', views.set),
    path('get', views.get),
    path("about/<name>", views.about),
    path("about", views.about),
    #запрос с возможностью ввести значения атрибутов
    path('about/<str:name>/<int:size>', views.about),
    
    path("index/<int:id>", views.index),
    path("access/<int:age>", views.access),
    path("vlozh/<int:id>", include(contact_patterns)), #вложенные маршруты (не работают)
    path("contact/", views.contact),
    path('shit', views.shit),
    path("data", views.data),

    path('options/', views.options),
    path('setting', views.setting),
    path("", views.main),
    path('cycles', views.cycles)
]
