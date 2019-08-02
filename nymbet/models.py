from django.db import models
from django.conf import settings
# Create your models here.



options = (
    ('victoire', 'Victoire'),
    ('Double chance', 'Double chance'),
    ('But', 'But'),
    )

class Championnat(models.Model):
    name    = models.CharField(max_length=40, unique=True)
    
 
    
    def __str__(self):
        return self.name

class Equipe1(models.Model):
    nom = models.CharField(max_length=40, unique=True)
     
    def __str__(self):
        return self.nom
    
class Equipe2(models.Model):
    nom = models.CharField(max_length=40, unique=True)
    
    def __str__(self):    
        return self.nom
    
class Match(models.Model):
    discipline = models.CharField(max_length=50)
    equipe1    = models.ForeignKey("Equipe1", on_delete=models.CASCADE)
    equipe2    = models.ForeignKey("Equipe2", on_delete=models.CASCADE)
    date       = models.DateField(auto_now=False, auto_now_add=False)
    heure      = models.TimeField(auto_now=False, auto_now_add=False)
    championnat    = models.ForeignKey("Championnat",on_delete=models.CASCADE)
   
    
    def __str__(self):    
        return self.equipe1.nom+ ' Vs '+self.equipe2.nom

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })
    
    
    
class Equipe1_opt(models.Model):
    nom_option = models.CharField(choices=options, max_length=50)
    cote1      = models.FloatField(max_length=3)
    equipe1    = models.ForeignKey('Equipe1', on_delete=models.CASCADE)
    match      = models.ForeignKey('Match', on_delete=models.CASCADE)
    
    def __str__(self):    
        return self.nom_option+'_'+self.equipe1.nom+ ' ( ' +self.match.equipe1.nom+ ' Vs '+self.match.equipe2.nom+' )'

class Equipe2_opt(models.Model):
    nom_option = models.CharField(choices=options, max_length=50)
    cote1      = models.FloatField(max_length=3)
    equipe2    = models.ForeignKey('Equipe2', on_delete=models.CASCADE)
    match      = models.ForeignKey('Match', on_delete=models.CASCADE)
    
    def __str__(self):    
        return self.nom_option+'_'+self.equipe2.nom+ ' ( ' +self.match.equipe1.nom+ ' Vs '+self.match.equipe2.nom+' )'
    
class Neutre(models.Model):
    nom    = models.CharField(max_length=50)
    cote1  = models.FloatField(max_length=3)
    match  = models.ForeignKey("Match", on_delete=models.CASCADE)
    
    def __str__(self):    
        return self.nom


    

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    solde = models.FloatField(default=10000)
    
    def __str__(self):
        return self.user.username


class Pronostic(models.Model):
    match = models.ForeignKey('Match', on_delete=models.CASCADE)
    v1    = models.IntegerField(max_length=2)
    nul   = models.IntegerField(max_length=2)
    v2    = models.IntegerField(max_length=2)

    def __str__(self):
        return self.match


