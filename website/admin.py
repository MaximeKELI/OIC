from django.contrib import admin
from .models import Article, Service, Projet, Contact, Page


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication', 'publie')
    list_filter = ('publie', 'date_creation')
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',)}
    date_hierarchy = 'date_creation'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ordre', 'actif')
    list_filter = ('actif',)
    search_fields = ('nom', 'description')


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_debut', 'statut', 'actif')
    list_filter = ('statut', 'actif', 'date_debut')
    search_fields = ('titre', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi', 'lu')
    list_filter = ('lu', 'date_envoi')
    search_fields = ('nom', 'email', 'sujet')
    readonly_fields = ('date_envoi',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('titre', 'afficher_dans_menu', 'ordre_menu')
    list_filter = ('afficher_dans_menu',)
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',)}
