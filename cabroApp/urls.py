from django.urls import path, include
from .views import create_type, create_col, update_type, delete_type, update_col, delete_col, connexion, deconnexion
from .views import create_project, update_project, delete_project, create_tache, update_tache, delete_tache, assigner_tache
from .views import telecharger_fichier, upload_fichier, delete_fichier
from .views import envoyer_message

urlpatterns = [
    #ATUTHENTIFICATION
    path('login/', connexion, name='connexion'),
    path('logout/', deconnexion, name='deconnexion'),
    #collaborateurs
    path('add_collaborateur/', create_col, name='create_col'),
    path('edit_col/<int:id>/', update_col, name='update_col'),
    path('delete_col/<int:id>/', delete_col, name='delete_col'),
    #typpe de collaborateurs
    path('add_type_collaborateur/', create_type, name='create_type'),
    path('edit_type/<str:code>/', update_type, name='update_type'),
    path('delete_type/<str:code>/', delete_type, name='delete_type'),
    #Projects
    path('add_project/', create_project, name='create_project'),
    path('project_details/<int:id>/', update_project, name='update_project'),
    path('delete_project/<int:id>/', delete_project, name="delete_project"),
    #Tache
    path('add_tache/<int:id>', create_tache, name="create_tache"),
    path('tache_details/<int:id>/', update_tache, name='update_tache'),
    path('delete_tache/<int:id>/', delete_tache, name='delete_tache'),
    path('assigner_tache/', assigner_tache, name="assigner_tache"),
    #PIÈCE JOINTE
    path('upload_fichier/<int:id>', upload_fichier, name="upload_fichier"),
    path('telecharger_fichier/<int:id>/', telecharger_fichier, name='telecharger_fichier'),
    path('delete_fichier/<int:id>/', delete_fichier, name='delete_fichier'),
    #Chat APP
    path("envoyer_message/<int:tache_id>/", envoyer_message, name="envoyer_message"),
    
]
