# Projet_Ros2
# Light Follower ROS2/Python Project

Ce projet est réalisé par le trinôme :
- **EL OUALI Mohamed**
- **Taleme Lina**
- **El Bouazzaoui Aya**

## Description du projet

Ce projet illustre un robot simple contrôlé par 3 packages de ROS2 et simulé à l'aide de *Turtlesim*. 

Étant donné nos connaissances modestes en ROS2, nous avons choisi Turtlesim comme environnement de simulation pour représenter :
- **La tortue principale** : un robot simulé qui suit les positions de lumière.
- **Light** : une deuxième tortue simulée représentant les sources lumineuses, dont la position change toutes les 2 secondes.

## Pré-requis

Avant de commencer, assurez-vous d'avoir installé :
- ROS2
- Le package *Turtlesim*
- Python 3.x

## Lancement de la simulation

Pour lancer la simulation :

1. Accédez au répertoire `ros2_ws` :
   ```bash
   cd ros2_ws
   ```

2. Exécutez le script Python nommé `launcher.py` :
   ```bash
   python3 launcher.py
   ```

## Fonctionnalités principales

- **Simulation de robot** : La tortue principale suit dynamiquement les mouvements de la lumière.
- **Mises à jour régulières** : La position de la lumière change toutes les 2 secondes pour tester le comportement du robot.

---

Merci pour votre intérêt envers notre projet !
