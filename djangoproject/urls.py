"""djangoproject URL Configuration

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
from django.urls import path, include

from .views import index, collaborateur, add_collaborateur, type_collaborateur, add_type_collaborateur, edit_collaborateur, edit_type_collaborateur
from .views import projects, add_project, project_details, add_tache, tache_details 
urlpatterns = [
    path('cabroApp/', include("cabroApp.urls")),
    path('admin/', admin.site.urls),
    path('', index),
    #collaborateurs
    path('collaborateur/', collaborateur),
    path('add-collaborateur/', add_collaborateur),
    path('edit_collaborateur/<int:id>/', edit_collaborateur),
    #typpe de collaborateurs
    path('type_collaborateur/', type_collaborateur),
    path('add_type_collaborateur/', add_type_collaborateur),
    path('edit_type_collaborateur/<str:code>/', edit_type_collaborateur),
    #PROJETS
    path('projects/', projects),
    path('add_project/', add_project),
    path('project_details/<int:id>/', project_details),
    #TÂCHES
    path('add_tache/<int:id>', add_tache),
    path('tache_details/<int:id>', tache_details),

    
]
