from django.shortcuts import render
from cabroApp.models import TypeCollaborateur, Collaborateur, Project, Tache, Piece_jointe, Assignation, Message
from django.contrib.auth.models import User



# AUTHENTIFICATION DU COLLABORATEUR
def index(request):
    return render(request, "login.html")


#COLLABORATEUR
def collaborateur(request):
    collaborateurs = Collaborateur.objects.all()
    users = User.objects.all()
    return render(request, "index.html", {'collaborateurs': collaborateurs, 'users':users})

def add_collaborateur(request):
    types = TypeCollaborateur.objects.all()
    return render(request, "ajouter_collaborateur.html", {'types': types})

def edit_collaborateur(request, id):
    # Récupérer le collaorateur à modifier
    collaborateur = Collaborateur.objects.get(pk=id)
    types = TypeCollaborateur.objects.all()
    
    # Rendu du formulaire avec les valeurs actuelles de l'enregistrement
    return render(request, 'update_collaborateur.html', {'collaborateur': collaborateur, 'types': types}) 


# TYPE DE COLLABORATEUR
def edit_type_collaborateur(request, code):
    # Récupérer le type à modifier
    type = TypeCollaborateur.objects.get(pk=code)
    
    # Rendu du formulaire avec les valeurs actuelles du collaborateur
    return render(request, "update_type_collaborateur.html", {'type': type})

def type_collaborateur(request):
    types = TypeCollaborateur.objects.all()
    return render(request, "type_collaborateur.html", {'types': types})

def add_type_collaborateur(request):
    return render(request, "ajouter_type_collaborateur.html")


# PROJECTS
def projects(request):
    user = request.user
    Projects = Project.objects.all()
    if user.is_superuser:
        return render(request, "projects/projects.html", {'projects':Projects})
    else:
        connect_col = Collaborateur.objects.get(pk=user.username)
        projects = Project.objects.filter(chef_id=connect_col.id)
        assigner = Assignation.objects.filter(collaborateur_id=connect_col.id)
        taches = Tache.objects.all()
        if len(projects) == 0:
            return render(request, "projects/taches.html", {'taches':taches, 'assigners':assigner})
        else:
            return render(request, "projects/projects.html", {'projects':projects, 'col':connect_col})
#Editer un projet
def project_details(request, id):
    collaborateurs = Collaborateur.objects.all()
    project = Project.objects.get(pk=id)
    taches = Tache.objects.filter(project_id=id)
    return render(request, "projects/project_details.html", {'project':project,  'taches':taches, 'collaborateurs': collaborateurs})
#Ajouter un projet
def add_project(request):
    collaborateurs = Collaborateur.objects.all()
    return render(request, "projects/add_project.html", {'collaborateurs': collaborateurs})


#TÂCHES

#Ajouter une tâche
def add_tache(request, id):
    
    return render(request, "projects/add_tache.html", {'project_id':id})
#Modifier une tache
def tache_details(request, id):
    tache = Tache.objects.get(pk=id)
    pieces = Piece_jointe.objects.filter(tache_id=id)
    project = Project.objects.get(pk=tache.project_id)
    collaborateurs = Collaborateur.objects.all()
    assignations = Assignation.objects.filter(tache_id=id)
    messages = Message.objects.filter(tache=id)
    return render(request, "projects/tache_details.html", {'tache':tache, 'pieces':pieces, 'project':project,'collaborateurs': collaborateurs, 'assignations':assignations, 'messages':messages})

    