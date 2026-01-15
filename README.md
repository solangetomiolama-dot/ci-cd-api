PROJET CI/CD PIPELINE AVEC API FLASK

Réalisé par :
- TOMI OLAMMA GABRIELLE SOLANGE HN5-CIN 21P643
- ZOO ZAME JESSICA 
- MINKOULOU ABE ALEXANDRE PATRICK
- DJEUMI NOUBET STEVE THIERRY

📌 Description du projet

Ce projet consiste à mettre en place un pipeline CI/CD complet pour une API Flask. Il couvre tout le cycle : développement, tests automatisés, containerisation avec Docker et déploiement continu sur Railway via GitHub Actions.

🎯 Objectifs du projet

Comprendre les principes du CI/CD

Automatiser les tests et le déploiement

Mettre en œuvre Docker pour la reproductibilité

Utiliser GitHub Actions pour l’intégration continue

Déployer une application en production (Railway)

🧰 Technologies utilisées

Python / Flask

Pytest

Git & GitHub

GitHub Actions

Docker

Railway

⚙️ Étapes de réalisation
🔹 1. Mise en place de l’environnement

Installation de Python, Git, création du dépôt GitHub, environnement virtuel, installation des dépendances et configuration du versionnement.

🔹 2. Développement de l’API Flask

Création d’une API simple avec deux routes principales :

/ → message de bienvenue

/status → vérification de l’état de l’API

Tests locaux pour valider le bon fonctionnement.

🔹 3. Tests automatisés & Intégration Continue

Implémentation de tests unitaires avec Pytest et configuration d’un pipeline GitHub Actions pour exécuter automatiquement les tests à chaque push.

🔹 4. Containerisation avec Docker

Création d’un Dockerfile pour empaqueter l’application, assurer sa portabilité et permettre le build automatique via le pipeline CI.

🔹 5. Déploiement continu avec Railway

Connexion du dépôt GitHub à Railway pour déclencher automatiquement le déploiement après chaque mise à jour validée.

📊 Résultats obtenus

API fonctionnelle et accessible en ligne

Pipeline CI/CD automatisé

Tests exécutés automatiquement

Image Docker générée avec succès

Déploiement continu opérationnel

⚠️ Difficultés rencontrées

Problèmes de versions Python

Erreurs de configuration YAML

Problèmes de Dockerfile

Configuration du déploiement Railway

👉 Tous ces problèmes ont été résolus grâce à l’analyse des logs, aux tests et aux corrections progressives.

🏁 Conclusion

Ce projet a permis de comprendre concrètement le fonctionnement d’un pipeline CI/CD moderne et l’importance de l’automatisation dans le développement et le déploiement des applications.

🔗 Liens utiles

Dépôt GitHub : https://github.com/solangetomiolama-dot/ci-cd-api

URL de production : https://ci-cd-api-production.up.railway.app/