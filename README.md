\# Projet CI/CD – Mini API



\## 📌 Présentation

Ce projet a pour objectif de mettre en place un pipeline CI/CD pour une mini application web (API).



Il montre comment automatiser les tests, le build et la préparation au déploiement à l’aide de GitHub Actions.





\## 🎯 Objectifs

\- Comprendre le fonctionnement du CI/CD  

\- Mettre en place un pipeline automatisé  

\- Créer une mini API pour support de tests  

\- Utiliser GitHub comme plateforme d’intégration



\# 🧰 Outils utilisés

\- Git \& GitHub  

\- Python (Flask)  

\- Pytest  

\- Docker  

\- GitHub Actions  





\## 🔹 Étape 1 – Mise en place de l’environnement



Dans cette étape, nous avons préparé l’environnement de travail et créé le dépôt du projet.



Actions réalisées :

\- installation de Python, Git, Docker et VS Code  

\- création du dépôt GitHub  

\- initialisation du dépôt local (`git init`)  

\- liaison avec GitHub (`git remote add origin ...`)  

\- vérification avec `git status`



Objectif :

Mettre en place le versionnement du code et préparer l’automatisation CI/CD.



Résultat :

Un dépôt GitHub fonctionnel prêt à recevoir le code.



\## 👥 Membres du groupe

* TOMI OLAMA GABRIELLE SOLANGE
* ZOO ZAME JESSICA
* MINKOULOU ABE ALEXANDRE PATRICK
* DJEUMI NOUBET STEVE THIERRY 



🔹 Étape 2 – Création de la mini API

1\. Objectif de l’étape



Cette étape avait pour objectif de créer une mini application web qui servira de support au pipeline CI/CD.

L’API permet de disposer d’un code réel sur lequel automatiser les tests, le build et la livraison.



2\. Création de l’environnement virtuel

python -m venv venv

venv\\Scripts\\activate





Ces commandes permettent de créer et d’activer un environnement virtuel Python.

Cela isole les bibliothèques du projet et évite les conflits avec d’autres projets.



3\. Installation des dépendances

pip install flask pytest





Flask est utilisé pour développer l’API.



Pytest est utilisé pour les tests automatiques dans la partie CI.



4\. Développement de l’API



Un fichier app.py a été créé.

Il contient deux routes principales :



/ : retourne un message de test



/status : retourne l’état de l’application



Le serveur est lancé avec :



python app.py





L’API est accessible sur http://localhost:5000.



5\. Sauvegarde des dépendances

pip freeze > requirements.txt





Cette commande génère un fichier listant toutes les bibliothèques nécessaires au projet.

Il est indispensable pour l’automatisation (Docker et CI/CD).



6\. Résultat de l’étape



À la fin de cette étape, le projet dispose :



d’une mini API fonctionnelle,



d’une base de code exploitable,



d’un fichier de dépendances,



d’un socle prêt pour l’intégration continue.



Cette API constitue le cœur applicatif du projet CI/CD.





Étape 3 – Mise en place des tests automatiques (CI)

1\. Objectif de l'étape

Cette étape vise à automatiser la vérification du code grâce à des tests unitaires et à configurer l'intégration continue avec GitHub Actions. L'objectif est de détecter rapidement les régressions.



2\. Création des tests unitaires

Un fichier test\_app.py a été créé avec trois tests :



Test de la route principale (/) : vérifie que l'API retourne le bon message



Test de la route status (/status) : vérifie que le statut est "OK"



Test d'une route inexistante : vérifie qu'une erreur 404 est retournée



3\. Exécution locale des tests

Les tests ont été exécutés localement avec pytest :



bash

pytest test\_app.py -v

Résultat : ✅ 3 tests passés avec succès.



4\. Configuration de GitHub Actions

Un pipeline CI a été configuré dans .github/workflows/ci.yml :



Déclenchement : à chaque push ou pull request sur la branche main



Environnement : Ubuntu avec Python 3.9



Étapes :



Récupération du code



Installation de Python



Installation des dépendances



Exécution des tests avec pytest



5\. Gestion des fichiers à ignorer

Un fichier .gitignore a été créé pour exclure :



L'environnement virtuel (venv/)



Les fichiers cache Python (\_\_pycache\_\_/)



Les fichiers de configuration d'IDE



6\. Résultat de l'étape

À la fin de cette étape, le projet dispose :



✅ De tests unitaires automatisés



✅ D'un pipeline CI configuré sur GitHub



✅ D'une structure propre avec .gitignore



✅ D'une base solide pour l'intégration continue

