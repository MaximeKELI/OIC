"""
URL configuration for oic_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]

# Configuration pour servir les fichiers statiques et média en développement
# En production, ces fichiers doivent être servis par le serveur web (nginx, Apache, etc.)
if settings.DEBUG:
    # En mode DEBUG, django.contrib.staticfiles sert automatiquement les fichiers
    # depuis STATICFILES_DIRS via le middleware StaticFilesHandler
    # On ajoute juste la configuration pour les fichiers média
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
