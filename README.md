GITHUB JSON LAUNCHER
====================

Structure du projet :

    main.py
    .scripts/
        1.py
        2.py
        3.py

Le dossier .scripts contient les scripts exécutés localement.
Le fichier JSON, lui, est hébergé sur GitHub.

CONFIGURATION
-------------

1. Dans l'invite de commande, rend toi dans le dossier du script et appelle le script avec comme argument config
2. (.python main.py config).

3. Sur GitHub, crée un fichier json avec cette mise en page :

   
    {
        "action": "2"
    }
   
   
(le json a deposer sur github est fourni dans cette repo)
(remplace le 2 par l'action que tu souhaite faire)

3.copie colle l'url de ton fichier json dans l'invite de commande (par exemple : https://github.com/TONNOM/TAREPO/main/config.json)

4. Lance :

    python main.py

Avec "action": "2", le programme lancera :

    .scripts/2.py

IMPORTANT
---------

Les fichiers 1.py, 2.py, 3.py, ... restent entièrement en local.
Seul config.json est téléchargé depuis GitHub.

Pour ajouter un nouveau script, par exemple x.py :

1. Ajoute .scripts/x.py
2. Ajoute "x": "x.py" dans le dictionnaire SCRIPTS de main.py.
