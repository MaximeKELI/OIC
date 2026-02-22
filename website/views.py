from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Article, Service, Projet, Contact, Page


def accueil(request):
    """Vue pour la page d'accueil"""
    articles = Article.objects.filter(publie=True)[:3]
    services = Service.objects.filter(actif=True)[:6]
    projets = Projet.objects.filter(actif=True)[:3]
    
    context = {
        'articles': articles,
        'services': services,
        'projets': projets,
    }
    return render(request, 'website/accueil.html', context)


def articles(request):
    """Vue pour la liste des articles"""
    articles_list = Article.objects.filter(publie=True)
    context = {
        'articles': articles_list,
    }
    return render(request, 'website/articles.html', context)


def article_detail(request, slug):
    """Vue pour le détail d'un article"""
    article = get_object_or_404(Article, slug=slug, publie=True)
    articles_recents = Article.objects.filter(publie=True).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'articles_recents': articles_recents,
    }
    return render(request, 'website/article_detail.html', context)


def services(request):
    """Vue pour la liste des services"""
    services_list = Service.objects.filter(actif=True)
    context = {
        'services': services_list,
    }
    return render(request, 'website/services.html', context)


def projets(request):
    """Vue pour la liste des projets"""
    projets_list = Projet.objects.filter(actif=True)
    context = {
        'projets': projets_list,
    }
    return render(request, 'website/projets.html', context)


def contact(request):
    """Vue pour la page de contact"""
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone', '')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')
        
        if nom and email and sujet and message:
            Contact.objects.create(
                nom=nom,
                email=email,
                telephone=telephone,
                sujet=sujet,
                message=message
            )
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
        else:
            messages.error(request, 'Veuillez remplir tous les champs obligatoires.')
    
    return render(request, 'website/contact.html')


def page_detail(request, slug):
    """Vue pour les pages statiques"""
    page = get_object_or_404(Page, slug=slug)
    context = {
        'page': page,
    }
    return render(request, 'website/page_detail.html', context)
