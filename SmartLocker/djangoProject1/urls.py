"""djangoProject1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from djangoProject1 import views

import djangoProject1.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', djangoProject1.views.home, name='home'),
    path('login/', djangoProject1.views.login, name='login'),
    path('signup/', djangoProject1.views.signup, name='signup'),
    path('login/new/', djangoProject1.views.new, name='new'),
    path('login/test/', djangoProject1.views.test, name='test'),
    #path('login/admin/', djangoProject1.views.admin, name='admin'),
    path('login/index', views.HomeView.as_view()),
    path('api', views.ChartData.as_view()),
    path('login/temp/', djangoProject1.views.temp, name='temp'),
    path('login/humi/', djangoProject1.views.humi, name='humi'),
]
