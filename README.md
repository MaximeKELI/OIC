# OIC International - Site Web Django

Site web moderne pour l'organisation OIC International spécialisée en agriculture.

## Installation

1. Créer un environnement virtuel (recommandé):
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Linux/Mac
# ou
venv\Scripts\activate  # Sur Windows
```

2. Installer les dépendances:
```bash
pip install -r requirements.txt
```

3. Effectuer les migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Créer un superutilisateur pour accéder à l'admin:
```bash
python manage.py createsuperuser
```

5. Lancer le serveur de développement:
```bash
python manage.py runserver
```

Le site sera accessible à l'adresse: http://127.0.0.1:8000/

L'interface d'administration Django sera accessible à: http://127.0.0.1:8000/admin/

## Structure du projet

- `oic_project/` - Configuration principale du projet Django
- `website/` - Application principale avec modèles, vues et templates
- `static/` - Fichiers statiques (CSS, JavaScript, images)
- `media/` - Fichiers média uploadés (créé automatiquement)

## Fonctionnalités

- **Page d'accueil** avec hero section, services, projets et actualités
- **Gestion des articles** (blog/actualités)
- **Gestion des services** offerts par l'organisation
- **Gestion des projets** agricoles
- **Formulaire de contact**
- **Pages statiques** personnalisables
- **Interface d'administration** Django complète
- **Design responsive** et moderne

## Base de données

Le projet utilise SQLite par défaut. La base de données sera créée automatiquement lors de la première migration.

## Personnalisation

Tous les contenus peuvent être gérés via l'interface d'administration Django après avoir créé un superutilisateur.
