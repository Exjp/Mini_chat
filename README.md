Compte-rendu Mini Chat :

Pour ce projet, nous avons utilisé comme outil Flask, Postgres pour les base de données et d'un navigateur internet.
Les langages utilisés sont le Python, le HTML, le CSS et le SQL.
Ce projet porte sur la création d'un D'un salon de discussion entre minimum 2 personnes. De ce fait le minimum requis pour ce projet est de pouvoir envoyer un message avec un pseudo et de voire ces messages. Pour accéder à ce chat, nous devions utiliser un navigateur internet en tant que client et flask en tant que serveur. Nous devions utiliser Postgres pour pouvoir avoir une base de donnée.
Pour cette base de donnée, nous utilisions un modèle entité avec 2 tableaux :
- Utilisateur (pseudo, mot de passe )
- Chat (pseudo, messages, Id)
Nous avons répartis le projet en 3 pages : une page de connexion, une page d'inscription et une page de discussion instantanée.
Toute ces pages sont faites en HTML et CSS.
La première page accessible est la page de connexion. Un formulaire a été utilisé pour pouvoir récupérer le pseudo et le mot de passe. Ainsi, on vérifie si le pseudo existe dans la table 'Utilisateur' et aussi si le mot de passe correspond au pseudo. Un boutont 'soummettre' permet faire cette vérification, ensuite, si tout est bon, la page de la discussion instantanée remplacera la page de connexion. Sinon la page de connexion sera rechargé avec le message d'erreur approprié. Pour pouvoir créer un nouveaux pseudo, un bouton 'Inscription' nous redirige vers une nouvelle page, la page d'inscription.
La page d'inscription contient un nouveau formulaire avec un pseudo et un mot de passe a rentré. Ces nouveaux pseudo et mot de passe sont introduite dans la table 'Utilisateur' par le bouton 'Soumettre'. Si on essaie de rajouter un pseudo déjà existant dans la table, nous serons redirigé vers la page de connexion avec un message d'erreur approprié. Si le pseudo est nouveau, alors nous serons redirigé vers la page de connexion pour ensuite l'utiliser.
Après avoir validé la page de connexion, nous nous trouvons sur la page du chat. Les 10 derniers messages posté sont affichés avec comme information, la position du message (l'ID), le pseudo et le message. Une zone de texte nous permet de rédiger notre message que nous pouvons posté grâce au bouton 'Soumettre'. Le pseudo utilisé pour se connecter au chat seras automatiquement mis à cotés du message posté. Ainsi la page sera mis à jour et le message sera affiché seulement pour l'utilisateur qui vient de le poster. Pour qu'un second utilisateur puisse voire le message, un bouton 'Refresh' qui nous permet de mettre à jour la page du chat. Enfin, un bouton 'Log out' nous permet de quitter le chat et de revenir à la page de connexion. De plus le pseudo sauvegardé lors de la connexion seras effacé de la session.
Les contraintes

- L'utilisation de nouvelles balises dans les fichiers HTML
- Ne reconnait pas les balises HTML pour les postes de messages
- Incapacité à ajouter l'heure et la date
- Ne peut pas mettre de guillemmets lors de la prise des pseudos (risque de bugs)
POURTIER jacques
WARDEH Amir