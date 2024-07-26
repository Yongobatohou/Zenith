from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .models import TypeCollaborateur, Collaborateur, Project, Tache, Piece_jointe, Assignation 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Message
# Create your views here.







# AUTHENTIFICATION

def connexion(request):
    if request.method == "POST":
        username = request.POST['id']
        password = request.POST['password']
        

        # Authentification de l'utilisateur
        user = authenticate(username=username, password=password)

        if user is not None:
            # Connexion de l'utilisateur
            login(request, user)
            use = request.user
            # Redirection vers une autre page
            if use.is_superuser:
                return redirect('/collaborateur/')
            else:
                return redirect('/projects/')
        else:
            # Erreur d'authentification
            return render(request, 'login.html', {'erreur_connexion': 'Identifiants incorrects'})

    return render(request, 'login.html')

def deconnexion(request):
    logout(request)
    return redirect('/')


# /////////////////////////////////////////////////////////////////////////


# TYPE DE COLLABORATEUR

    #Création d'un nouveau type de collaborateur
def create_type(request):
    if request.method == "POST":
        code = request.POST['code']
        nom = request.POST['nom']
        
        type = TypeCollaborateur(code=code, nom=nom)
        
        type.save()
        
        return redirect('/type_collaborateur/')
    return render(request, 'ajouter_type_collaborateur.html')

    #Mise à jour d'un type de collaborateur
def update_type(request, code):
    
    type = TypeCollaborateur.objects.get(code=code)
    
    if request.method == "POST":
        code = request.POST['code']
        nom = request.POST['nom']
        
        type.code = code
        type.nom = nom
        
        type.save()
        
        return redirect('/type_collaborateur/')
    return render(request, 'type_collaborateur.html')

    #Suppression d'un type de collaborateur
def delete_type(code):
    
    type = TypeCollaborateur.objects.get(pk=code)
    
    type.delete()
    
    return redirect('/type_collaborateur/')
   
   
#COLLABORATEUR

    #Création d'un collaborateur    
def create_col(request):
    if request.method == "POST":
        
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        burnDate = request.POST['burnDate']
        password = request.POST['password']
        confirm = request.POST['password_confirmation']
        level = request.POST['level']
        type = request.POST['type']
        
        if password==confirm:
            
            user = User.objects.create_user(username=nom,password=password, first_name=prenom, last_name=nom)
            collaborateur = Collaborateur(user=user, 
                                      nom=nom, 
                                      prenom=prenom, 
                                      date_naiss=burnDate, 
                                      mot_passe=password,
                                      niveau_etude=level,
                                      type=type)
            collaborateur.save()
            
            return redirect('/collaborateur/')
        else:
            error = "Mot de passe non confirmé"
        
    return render(request, 'ajouter_collaborateur.html', {'erreur':error})


    #Mise à jour d'un collaborateur
def update_col(request, id):
    
    collaborateur = Collaborateur.objects.get(pk=id)
    user = User.objects.get(username=id)
    
    if request.method == "POST":
        
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        burnDate = request.POST['burnDate']
        password = request.POST['password']
        confirm = request.POST['password_confirmation']
        level = request.POST['level']
        type = request.POST['type']
        
        if password==confirm:
        
            user.password=password
            user.first_name=prenom
            user.last_name=nom
            user.save()
            
            
            collaborateur.nom = nom 
            collaborateur.prenom = prenom 
            collaborateur.date_naiss = burnDate 
            collaborateur.mot_passe = password 
            collaborateur.niveau_etude = level
            collaborateur.type=type
            collaborateur.user=user
            
            collaborateur.save()
            
            return redirect('/collaborateur/')
        else:
            error = "Mot de passe non confirmé"
            return render(request, 'update_collaborateur.html', {'collaborateur': collaborateur, 'erreur':error})
            
    return render(request, 'index.html', {'collaborateur': collaborateur})


    #Suppression d'un collaborateur
def delete_col(request, id):
    
    collaborateur = Collaborateur.objects.get(pk=id)
    user = User.objects.get(username=id)
    
    collaborateur.delete()
    user.delete()
    return redirect('/collaborateur/')



#PROJECTS

#Création de projets   
def create_project(request):
    if request.method == "POST":
        
        titre = request.POST['titre']
        description = request.POST['description']
        chef = request.POST['chef']
        
        project = Project(titre=titre,
                          description=description,
                          chef_id=chef)
        
        project.save()
            
        return redirect('/projects/')
       
        
    return render(request, 'projects/add_project.html')

#Mettre à jour les information d'un projet
def update_project(request, id): 
    if request.method == "POST":
        project = Project.objects.get(pk=id)
        
        titre = request.POST['titre']
        description = request.POST['description']
        chef = request.POST['chef']
        
        project.titre=titre
        project.description=description
        project.chef_id=chef
        
        project.save()
            
        return redirect(request.META['HTTP_REFERER'])
       
        
    return render(request, 'projects/project_details.html/{{project.id}}')

#Suppromer un projet
def delete_project(request, id):
    
    project = Project.objects.get(pk=id)
    
    project.delete()
    
    return redirect('/projects/')



#Tâches

#Création de tâches   
def create_tache(request, id):  
    if request.method == "POST":
        
        libelle = request.POST['libelle']
        description = request.POST['description']
        delai = request.POST['delai']
        date_debut = request.POST['date_debut']
        tache = Tache(libellé=libelle,
                          description=description,
                          date_debut=date_debut,
                          delai=delai,
                          project_id=id)
        
        tache.save()
            
        return redirect(f"/project_details/{id}")
       
        
    return render(request, 'projects/add_tache.html')

#Mettre à jour les information d'une tache
def update_tache(request, id): 
    if request.method == "POST":
        tache = Tache.objects.get(pk=id)
        
        libelle = request.POST['libelle']
        description = request.POST['description']
        delai = request.POST['delai']
        date_debut = request.POST['date_debut']
        date_fin = request.POST['date_fin']
        statut = request.POST['statut']
        
        
        tache.libellé=libelle
        tache.description=description
        tache.delai=delai
        tache.date_debut=date_debut
        tache.date_fin=date_fin
        tache.statut=statut
        
        tache.save()
            
        return redirect(request.META['HTTP_REFERER'])
       
       
        
    return render(request, request.META['HTTP_REFERER'])

#Supprimer une tache
def delete_tache(request, id):
    
    tache = Tache.objects.get(pk=id)
    
    tache.delete()
    
    return redirect(request.META['HTTP_REFERER'])

def assigner_tache(request):
    
    if request.method == "POST":
        
        tache = request.POST['tache_id']
        col = request.POST['collaborateur']
        assigner = Assignation(tache_id=tache, collaborateur_id=col)
        
        assigner.save()
    return redirect(request.META['HTTP_REFERER'])
        
        
#PIÈCES JOINTES

#Ajouter une pièce jointe
def upload_fichier(request, id):
    if request.method == 'POST':
        fichier = request.FILES['fichier']
        nom = request.POST['nom']

        nouveau_fichier = Piece_jointe(file=fichier, titre=nom, tache_id=id)
        nouveau_fichier.save()

        return redirect(request.META['HTTP_REFERER'])

def telecharger_fichier(request, id):
    fichier = Piece_jointe.objects.get(pk=id)

    response = HttpResponse(fichier.file, content_type=fichier.file)
    response['Content-Disposition'] = f'attachment; filename="{fichier.titre}"'

    return response

def delete_fichier(request, id):
    fichier = Piece_jointe.objects.get(pk=id)
    fichier.delete()

    return redirect(request.META['HTTP_REFERER'])

#Chat APP

@login_required
def envoyer_message(request, tache_id):
    if request.method == "POST":
        contenu = request.POST["contenu"]

        message = Message(
            expediteur=request.user,
            tache=Tache.objects.get(pk=tache_id),
            contenu=contenu,
        )
        message.save()

    return redirect(request.META['HTTP_REFERER'])

