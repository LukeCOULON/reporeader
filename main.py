import json
import os
import subprocess
import sys
import urllib.request

CONFIG_URL_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    ".config_url"
)

DEFAULT_GITHUB_JSON_URL = (
    "https://raw.githubusercontent.com/"
    "LukeCOULON/reporeader/main/config.json"
)

SCRIPTS = {
    "1": "1.py",
    "2": "2.py",
    "3": "3.py",
}


def convertir_url_github(url):

    url = url.strip()

    prefix = "https://github.com/"

    if not url.startswith(prefix):
        raise ValueError(
            "L'URL doit commencer par https://github.com/"
        )

    chemin = url[len(prefix):]

    if "/blob/" not in chemin:
        raise ValueError(
            "L'URL GitHub doit contenir '/blob/'.\n"
            "Exemple :\n"
            "https://github.com/user/repo/blob/main/config.json"
        )

    chemin = chemin.replace("/blob/", "/", 1)

    return "https://raw.githubusercontent.com/" + chemin


def sauvegarder_url(url):

    with open(CONFIG_URL_FILE, "w", encoding="utf-8") as fichier:
        fichier.write(url)


def charger_url():

    if not os.path.isfile(CONFIG_URL_FILE):
        return DEFAULT_GITHUB_JSON_URL

    with open(CONFIG_URL_FILE, "r", encoding="utf-8") as fichier:
        url = fichier.read().strip()

    if not url:
        return DEFAULT_GITHUB_JSON_URL

    return url


def mode_config():

    url = input("> ").strip()
    if not url:
        print("[ERREUR] Aucune URL fournie.")
        return

    try:
        url_raw = convertir_url_github(url)
    except ValueError as e:
        print(f"[ERREUR] {e}")
        return

    print("URL Raw GitHub générée :")
    print(url_raw)

    sauvegarder_url(url_raw)


def lire_json_github():

    github_json_url = charger_url()
    with urllib.request.urlopen(
        github_json_url,
        timeout=10
    ) as response:
        contenu = response.read().decode("utf-8")

    return json.loads(contenu)


def lancer_script(action):

    script = SCRIPTS.get(str(action))

    if script is None:
        print(f"[ERREUR] Action inconnue : {action}")
        return

    dossier_scripts = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        ".scripts"
    )

    script_path = os.path.join(dossier_scripts, script)

    if not os.path.isfile(script_path):
        print(f"[ERREUR] Script introuvable : {script_path}")
        return

    try:
        subprocess.run(
            [sys.executable, script_path],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(
            f"[ERREUR] {script} s'est terminé "
            f"avec le code {e.returncode}"
        )


def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "config":
        mode_config()
        return

    try:
        config = lire_json_github()
    except Exception as e:
        print(f"[ERREUR] Impossible de lire le JSON GitHub : {e}")
        return

    action = config.get("action")

    if action is None:
        print("[ERREUR] La clé 'action' est absente du JSON.")
        return

    lancer_script(action)


if __name__ == "__main__":
    main()