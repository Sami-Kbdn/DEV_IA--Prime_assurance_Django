# <p align="center">Prédiction de Prime d'Assurance</p>
<p align="center">
    <img src="images/project_logo.png" alt="Pas de logo pour ce projet" width="200">
</p>

## ➤ Menu

* [➤ Project Structure](#-project-structure)
* [➤ How to Run](#-how-to-run)
* [➤ Requirements](#-requirements)

---

## Project Structure

Ce projet inclut les fichiers et modules principaux suivants :

- **manage.py**: Le fichier principal de gestion du projet Django, permettant de gérer les migrations, les commandes et le serveur.
- **tailwind_config.py**: Configuration pour `tailwindcss` pour la gestion du style de l'application.
- **requirements.txt**: Liste des dépendances nécessaires au projet.

### Modules supplémentaires

- **whitenoise**: Permet de gérer et de servir des fichiers statiques efficacement.
- **Modeles de Machine Learning**: Contient les fichiers et modèles utilisés pour prédire les primes d'assurance.

---

## How to Run

Suivez ces étapes pour exécuter le projet :

1. **Assurez-vous que Python (ou les dépendances requises) est installé sur votre système.**
2. Clonez ce dépôt sur votre machine locale :

        git clone https://github.com/NicoCasso/Application_Django_Prediction.git


    Allez dans le répertoire du projet :

        cd MyApp

    Créez et activez un environnement virtuel :

        python -m venv .venv
        source .venv/bin/activate  # Sur macOS/Linux
        .venv\Scripts\activate     # Sur Windows

    Installez les dépendances nécessaires :

        pip install -r requirements.txt

    Initialisez et configurez tailwindcss :

        python manage.py tailwind init
        python manage.py tailwind install

    Collectez les fichiers statiques via whitenoise :

        python manage.py collectstatic

    Créez la base de données :

        python manage.py makemigrations
        python manage.py migrate

    Créez un super utilisateur :

        python manage.py createsuperuser

    Lancez le serveur tailwind dans un terminal :

        python manage.py tailwind start

    Lancez le serveur Django dans un autre terminal :

        python manage.py runserver

---

## Requirements

Voici la liste des logiciels, bibliothèques et dépendances nécessaires pour exécuter ce projet :

    Python >= 3.12
    pandas >= 2.2.3
    scikit-learn >= 1.6.1
    django >= 5.1.5

https://www.djangoproject.com/

    django-tailwind >= 3.8.0
    django-browser-reload >= 1.17.0

https://django-tailwind.readthedocs.io/en/latest/installation.html

    python-dotenv >= 1.0.1

https://configu.com/blog/using-py-dotenv-python-dotenv-package-to-manage-env-variables/

    whitenoise >= 6.8.2

https://whitenoise.readthedocs.io/en/stable/django.html

## Outputs

Les utilisateurs peuvent s'attendre aux sorties suivantes :

    Interface utilisateur : Un site internet dans lequel les utilisateurs peuvent s'sincrire, renseigner des informations personnelles et accéder aux informations de prédiction d'assurance.

    Prédictions : Les résultats des prédictions (en $) des primes d'assurance annuelles basés sur les données d'entrée.







