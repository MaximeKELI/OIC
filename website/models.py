from django.db import models
from django.utils import timezone


class Article(models.Model):
    """Modèle pour les articles/blog"""
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    date_creation = models.DateTimeField(default=timezone.now)
    date_publication = models.DateTimeField(blank=True, null=True)
    publie = models.BooleanField(default=False)
    auteur = models.CharField(max_length=100, default='OIC')
    
    class Meta:
        ordering = ['-date_publication', '-date_creation']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    
    def __str__(self):
        return self.titre


class Service(models.Model):
    """Modèle pour les services offerts"""
    nom = models.CharField(max_length=200)
    description = models.TextField()
    icone = models.CharField(max_length=100, help_text="Nom de l'icône (ex: fa-seedling)")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    ordre = models.IntegerField(default=0)
    actif = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['ordre', 'nom']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.nom


class Projet(models.Model):
    """Modèle pour les projets agricoles"""
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/', blank=True, null=True)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    statut = models.CharField(
        max_length=20,
        choices=[
            ('en_cours', 'En cours'),
            ('termine', 'Terminé'),
            ('planifie', 'Planifié'),
        ],
        default='planifie'
    )
    actif = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-date_debut']
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
    
    def __str__(self):
        return self.titre


class Contact(models.Model):
    """Modèle pour les messages de contact"""
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(default=timezone.now)
    lu = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_envoi']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return f"{self.nom} - {self.sujet}"


class Page(models.Model):
    """Modèle pour les pages statiques"""
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    contenu = models.TextField()
    afficher_dans_menu = models.BooleanField(default=True)
    ordre_menu = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['ordre_menu', 'titre']
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
    
    def __str__(self):
        return self.titre
