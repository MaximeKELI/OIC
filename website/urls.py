from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('articles/', views.articles, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('services/', views.services, name='services'),
    path('projets/', views.projets, name='projets'),
    path('contact/', views.contact, name='contact'),
    path('pages/<slug:slug>/', views.page_detail, name='page_detail'),
]
