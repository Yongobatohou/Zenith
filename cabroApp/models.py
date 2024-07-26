from django.db import models
from django.contrib.auth.models import User
from random import randint

# Create your models here.

def generate_id():
        return randint(100000, 999999)

class Collaborateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.CharField(primary_key=True, max_length=6, default=generate_id)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=200)
    date_naiss = models.DateField( auto_now=False, auto_now_add=False, )
    mot_passe = models.CharField(max_length=8)
    niveau_etude = models.CharField(max_length=100)
    id_demande_stage = models.CharField(max_length=50, null=True)
    date_enregistre = models.DateTimeField( auto_now=False, auto_now_add=True)
    status = models.BooleanField( null=True)
    type = models.CharField(max_length=10, default="STAGIAIRE")
    
    def save(self):
        if not self.id:
            self.id = models.AutoField.generate_default(self)
        self.user.username = str(self.id)
        self.user.save()
        super().save()
    
class TypeCollaborateur(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=50)
    
#GESTION DES PROJETS ET TÂCHES
    
    #Gestion des tâches
class Tache(models.Model):
    libellé = models.CharField(max_length=50)
    description = models.TextField(null=False)
    date_debut = models.DateField( auto_now=False, auto_now_add=False)
    delai = models.CharField( max_length=2)
    date_fin = models.DateField(auto_now=False, auto_now_add=False, null=True) 
    statut = models.CharField(max_length=50, default='En cours')
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    
    
class Piece_jointe(models.Model):
    titre = models.CharField(max_length=50)
    file = models.FileField(upload_to='pièces-jointes/', max_length=100)
    date_upload = models.DateField(auto_now=False, auto_now_add=True)
    tache = models.ForeignKey("Tache", on_delete=models.CASCADE)
    
    #Gestion des projets

class Project(models.Model):
    titre = models.CharField(max_length=50)
    description = models.TextField(null=False)
    chef = models.ForeignKey("Collaborateur", on_delete=models.CASCADE)
    
    
class Assignation(models.Model):
    collaborateur = models.ForeignKey("Collaborateur", on_delete=models.CASCADE)
    tache = models.ForeignKey("Tache", on_delete=models.CASCADE)
    
#Messages
class Message(models.Model):
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE)
    tache = models.ForeignKey("Tache", on_delete=models.CASCADE)
    contenu = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

