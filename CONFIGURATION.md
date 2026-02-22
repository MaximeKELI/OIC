# Configuration Django - Full Django Native

Ce projet utilise une configuration 100% Django native pour tous les aspects.

## Configuration des fichiers statiques

### Settings (settings.py)

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
```

### URLs (urls.py)

En mode DEBUG, Django sert automatiquement les fichiers statiques via `django.contrib.staticfiles` qui est dans `INSTALLED_APPS`. Aucune configuration supplémentaire n'est nécessaire pour les fichiers statiques.

Pour les fichiers média (uploads), on utilise :
```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Comment ça fonctionne

1. **En développement (DEBUG=True)** :
   - Django sert automatiquement les fichiers depuis `STATICFILES_DIRS` via le middleware `StaticFilesHandler`
   - Les fichiers sont servis directement depuis le dossier `static/`
   - Aucune commande `collectstatic` nécessaire

2. **En production (DEBUG=False)** :
   - Exécuter `python manage.py collectstatic` pour collecter tous les fichiers dans `STATIC_ROOT`
   - Le serveur web (nginx, Apache) sert les fichiers depuis `STATIC_ROOT`
   - Django ne sert plus les fichiers statiques

## Utilisation dans les templates

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/main.js' %}"></script>
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

## Vérification

Pour vérifier que tout fonctionne :
```bash
python manage.py check
python manage.py findstatic css/style.css
```

## Avantages de cette configuration

- ✅ 100% Django native
- ✅ Pas de configuration manuelle nécessaire
- ✅ Fonctionne automatiquement en développement
- ✅ Prêt pour la production avec collectstatic
- ✅ Suit les meilleures pratiques Django
