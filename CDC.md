# Cahier des charges BasketScorer

## But
L'objectif est de créer une application mobile dont l'objectif est de compter les points lors d'un match de basket-ball.

## Fonctionnalités
A partir de la caméra du téléphone, compte les points d'un match de basket en live.
Affiche sur le téléphone le score en temps réel.

## Étapes du projet avec TDD

1. **Définir les exigences et les histoires d'utilisateur**
   1. **Chronomètre de Jeu**
      - **Exigence**: L'application doit permettre à l'utilisateur de démarrer, arrêter et réinitialiser un chronomètre pour suivre la durée d'un match.
      - **Histoire d'Utilisateur**: En tant qu'utilisateur, je veux pouvoir démarrer un chronomètre afin de suivre le temps de jeu.

   2. **Capture de Points**
      - **Exigence**: L'application doit utiliser la caméra pour détecter et compter les points marqués pendant le match.
      - **Histoire d'Utilisateur**: En tant qu'utilisateur, je veux capturer les points marqués à l'aide de la caméra afin que le score soit mis à jour automatiquement.

   3. **Affichage du Score**
      - **Exigence**: L'application doit afficher le score en temps réel sur l'écran de l'utilisateur.
      - **Histoire d'Utilisateur**: En tant qu'utilisateur, je veux voir le score actuel sur mon téléphone afin de savoir qui mène le match.

2. **Configurer la structure du projet**
    BasketScorer/
    │
    ├── src/                    # Code source
    │   ├── main.py             # Point d'entrée de l'application
    │   ├── camera.py           # Gestion de la caméra
    │   ├── score_tracker.py     # Logique de comptage de points
    │   └── display.py          # Affichage du score
    │
    ├── tests/                  # Tests unitaires
    │   ├── test_camera.py      # Tests pour la gestion de la caméra
    │   ├── test_score_tracker.py # Tests pour le suivi des points
    │   └── test_display.py     # Tests pour l'affichage du score
    │
    ├── docs/                   # Documentation du projet
    │   └── README.md           # Documentation principale
    │
    └── requirements.txt        # Dépendances du projet

3. **Écrire des tests initiaux**
   - Pour chaque histoire d'utilisateur, écrire des tests qui définissent le comportement attendu de l'application. Par exemple :
     - Tester si l'application peut démarrer un jeu.
     - Tester si la caméra peut capturer des points.

4. **Implémenter les fonctionnalités**
   - Commencer à implémenter les fonctionnalités requises pour passer les tests. Cela peut inclure :
     - Intégration de la fonctionnalité de caméra.
     - Création d'un système de score.

5.  **Exécuter des tests et refactoriser**
   - Après avoir implémenté chaque fonctionnalité, exécuter les tests pour s'assurer qu'ils passent.
   - Refactoriser le code pour une meilleure lisibilité et maintenabilité.

6.  **Itérer**
   - Continuer le cycle d'écriture de tests, d'implémentation de fonctionnalités et de refactorisation jusqu'à ce que toutes les histoires d'utilisateur soient complètes.

7.  **Documentation et tests finaux**
   - Documenter l'application et son utilisation.
   - Effectuer des tests finaux pour s'assurer que tout fonctionne comme prévu.