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

1. Ouvre main.py.

2. Au début du fichier, modifie :

    GITHUB_JSON_URL = "https://raw.githubusercontent.com/TON_COMPTE/TON_REPO/main/config.json"

   avec l'URL RAW de ton fichier config.json.

3. Sur GitHub, crée par exemple :

    {
        "action": "2"
    }

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
