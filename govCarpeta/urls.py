"""govCarpeta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from govCarpeta.views import index, registerCitizen, authenticateDocument, validateCitizen, loginCitizen, logoutUser, signUpCitizen, fileExplorer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginCitizen),
    path('login/', loginCitizen, name='loginCitizen'),
    path('register/', signUpCitizen, name='signUpCitizen'),
    path('main/', index, name='index'),
    path('registerCitizen/', registerCitizen, name='registerCitizen'),
    path('authenticateDocument/', authenticateDocument, name='authenticateDocument'),
    path('validateCitizen/', validateCitizen, name='validateCitizen'),
    path('fileExplorer/', fileExplorer, name='fileExplorer'),
    path('logout/', logoutUser, name='logout'),
]
