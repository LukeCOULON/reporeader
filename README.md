# GitHub JSON Launcher

Un petit lanceur Python permettant d'exécuter **localement** différents scripts en fonction d'une configuration stockée sur **GitHub**.

## Structure du projet

```text
main.py
.scripts/
├── 1.py
├── 2.py
└── 3.py
```

* Le dossier `.scripts/` contient les scripts exécutés localement.
* Le fichier `config.json` est hébergé sur GitHub.
* `main.py` récupère la configuration depuis GitHub et lance le script correspondant.

## Configuration

### 1. Configurer le lanceur

Ouvre une invite de commande dans le dossier du projet, puis exécute :

```bash
python main.py config
```

Le programme te demandera ensuite l'URL du fichier JSON hébergé sur GitHub.

### 2. Créer le fichier JSON sur GitHub

Crée un fichier `config.json` avec la structure suivante :

```json
{
    "action": "2"
}
```

> Le fichier JSON prêt à être utilisé est également fourni dans ce dépôt.

La valeur de `action` correspond au script à exécuter.

Par exemple :

* `"action": "1"` → `.scripts/1.py`
* `"action": "2"` → `.scripts/2.py`
* `"action": "3"` → `.scripts/3.py`

### 3. Indiquer l'URL du fichier JSON

Copie-colle l'URL de ton fichier `config.json` lorsque le programme te le demande.

Exemple :

```text
https://github.com/TONNOM/TAREPO/main/config.json
```

### 4. Lancer le programme

Une fois la configuration enregistrée, exécute simplement :

```bash
python main.py
```

Si le fichier JSON contient :

```json
{
    "action": "2"
}
```

le programme exécutera automatiquement :

```text
.scripts/2.py
```

## Ajouter un nouveau script

Pour ajouter un nouveau script, par exemple `x.py` :

1. Ajoute le fichier dans `.scripts/` :

```text
.scripts/x.py
```

2. Ajoute la correspondance dans le dictionnaire `SCRIPTS` de `main.py` :

```python
"x": "x.py"
```

3. Utilise ensuite cette action dans `config.json` :

```json
{
    "action": "x"
}
```

Le lanceur exécutera alors :

```text
.scripts/x.py
```

## Important

Les scripts `1.py`, `2.py`, `3.py`, etc. restent **entièrement en local**.

Le seul fichier récupéré depuis GitHub est :

```text
config.json
```

GitHub sert donc uniquement à **déterminer quelle action doit être exécutée**. Les scripts eux-mêmes ne sont jamais téléchargés depuis GitHub.
