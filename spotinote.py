import os
import sphinx
from time import sleep
from datetime import datetime
import base64
import requests
from colorama import *
# Spotipy import
import spotipy


# Instagrapi Imports
from instagrapi import *
from dotenv import load_dotenv
init(autoreset=True)
os.system('cls')
def print_welcome_message():
    MOTD = ''' AMÉLIORÉ MIS A JOUR ET TRADUIT EN FRANCAIS PAR ARCHLUKY projet Original ici >> https://github.com/nil-malh/Notify/  : '''

    print(Fore.CYAN + Style.BRIGHT + MOTD)
    print(  Fore.BLUE + Style.BRIGHT + " en cas de besoin contacte archluky sur instagam")


def debug(message):
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"[{timestamp}] : {message}")


def setup_env_file():
    if not os.path.isfile(".env"):
        client_id = input(  Fore.GREEN + Style.BRIGHT + "entre l'id client de ton bot spotify \n" )
        client_secret = input( Fore.YELLOW + "entre ton id client secret de bot spotify \n")
        print(f' {Fore.RED + Style.BRIGHT} Pour trouver ton jeton de rafraîchissement, va sur https://spotify-refresh-token-generator.netlify.app/ (pense bien à activer toutes les options [scope]')
        refresh_token = input(  Fore.MAGENTA + Style.BRIGHT + "entre ton jeton de rafraichissement obtenu sur le site juste au dessus\n")
        bot_refresh_rate = input(  Fore.GREEN + Style.BRIGHT +  "entre le nombre de seconde avant d'actualisé la note instagram (150 conseillé pour éviter d'être bloqué par l'api instagram\n) ")
        note_prefix = input(  Fore.YELLOW + Style.BRIGHT +  "écrit ce que tu veux comme préfix au début de la note  { <préfixe> (titre) <séparateur> (artiste) }\n")
        separator = input(  Fore.MAGENTA + Style.BRIGHT + "entre le sépartaeur entre l'artiste et le nom du titre  { <préfixe> (titre) <séparateur> (artiste) }\n ")
        ig_username = input(  Fore.GREEN + Style.BRIGHT + "entre ton pseudo instagram")
        ig_password = input(  Fore.YELLOW + Style.BRIGHT + "entre ton mot de passe instagram")

        if not bot_refresh_rate:
            debug(  Fore.CYAN + Style.BRIGHT + "automatiquement mis en actualisation 150s")
            bot_refresh_rate = "150"

        with open(".env", "w") as env_file:
            env_file.write(f"SPOTIPY_CLIENT_ID={client_id}\n")
            env_file.write(f"SPOTIPY_CLIENT_SECRET={client_secret}\n")
            env_file.write(f"SPOTIPY_REFRESH_TOKEN={refresh_token}\n")
            env_file.write(f"BOT_REFRESH_RATE={bot_refresh_rate}\n")
            env_file.write(f'SONG_SEPARATOR={separator}')
            env_file.write(f"IG_USERNAME={ig_username}\n")
            env_file.write(f"IG_PASSWORD={ig_password}\n")
            env_file.write(f"IG_NOTE_PREFIX={note_prefix}\n")


print_welcome_message()
setup_env_file()
load_dotenv()

debug("chagrement depuis le ficher .env  ...")
load_dotenv()
debug("compte chargé !")

# configuration et compte instagram
IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")
IG_NOTE_PREFIX = os.getenv("IG_NOTE_PREFIX")
IG_CREDENTIAL_PATH = './ig_settings.json'

SLEEP_TIME = os.getenv("BOT_REFRESH_RATE")  # in seconds
SONG_SEPARATOR = os.getenv("SONG_SEPARATOR")
# Connection à spotify
SPOTIFY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIFY_REFRESH_TOKEN = os.getenv("SPOTIPY_REFRESH_TOKEN")

if not all([SPOTIFY_CLIENT_SECRET, SPOTIFY_CLIENT_ID, SPOTIFY_REFRESH_TOKEN]):
    raise Exception(  Fore.RED + Style.BRIGHT +  "impossible de trouvé le compte instagram dans le ficher .env")
if not SONG_SEPARATOR:
    SONG_SEPARATOR = "-"

def get_access_token(client_id, client_secret, refresh_token):
    debug("entative de connection à l'api spotify ...")
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }
    auth = f"{client_id}:{client_secret}"
    auth = auth.encode("utf-8")
    auth = base64.b64encode(auth).decode("utf-8")
    response = requests.post("https://accounts.spotify.com/api/token", data=data,
                             headers={
                                 "Authorization": f"Basic {auth}",
                             })

    if response.status_code != 200:
        raise Exception(f' {Fore.RED}{Style.BRIGHT} "requète echoué.. code erreur :  {response.status_code}:{response.text}')
    response_data = response.json()
    access_token = response_data["access_token"]
    debug("le jeton api Spotify à bien été régénéré !")
    return access_token


access_token = get_access_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REFRESH_TOKEN)
sp = spotipy.Spotify(auth=access_token)


class Bot:
    _cl = None

    def __init__(self):
        self._cl = Client()

        if not all([IG_USERNAME, IG_PASSWORD, IG_NOTE_PREFIX,IG_CREDENTIAL_PATH]):
            raise Exception("impossible de trouvé le compte instagram dans le ficher .env ")
        if os.path.exists(IG_CREDENTIAL_PATH):
            self._cl.load_settings(IG_CREDENTIAL_PATH)
            debug(f'connection à instagram sur le compte :  {IG_USERNAME}')
            self._cl.login(IG_USERNAME, IG_PASSWORD)
        else:
            TOTA = input("entre ton code d'a2f si tu en à un sinon appuis sur entrée")
            debug(f'connection à  {IG_USERNAME} pour la 1ere fois : {TOTA}')
            self._cl.login(IG_USERNAME, IG_PASSWORD, verification_code=TOTA)
            debug(f'Logged-in to Instagram !')
            self._cl.dump_settings(IG_CREDENTIAL_PATH)
            debug('le compte à bien été sauvegadé !')

    def send_music_note(self, song_name, artist,separator):

        previous_note = None
        note_content = f"{IG_NOTE_PREFIX} {song_name} {separator} {artist}" if IG_NOTE_PREFIX else f"🎧  {song_name} {separator} {artist}"
        if note_content == previous_note and previous_note is not None:
            debug("Le contenue de la note est le même pas de changement")
        if len(note_content) < 60:
            self._cl.create_note(f"{IG_NOTE_PREFIX} : {song_name} {separator} {artist}" if IG_NOTE_PREFIX else f"🎧 : {song_name} {separator} {artist}", 0)
            previous_note = note_content

        else:
            print(f'la note est trop longue (60 caratères maximum) peu être modifié le préfixe si cette erreur arrivé souvent. (note_content_len : {len(note_content)})')

    

    def update(self, spotify):
        current_track = spotify.current_playback()

        if current_track:
            # Si une musique est actuellement en cours de lecture
            song_name = current_track["item"]["name"]
            artist = current_track["item"]["artists"][0]["name"]
            note_content = f"{song_name} - {artist}"
            debug(note_content)
            debug("Envoi de la note.")
            bot.send_music_note(song_name, artist, SONG_SEPARATOR)
            debug(f'La note est publiée sur le compte : {IG_USERNAME} ! ')
        else:
            # Aucune musique en cours de lecture, supprimer la note
            if self._cl.user_id:
                # Récupérer les notes de l'utilisateur
                notes = self._cl.get_notes()
                if notes:
                    latest_note = notes[0]
                    self._cl.delete_note(latest_note.id)
                    debug("Note supprimée car aucune musique en cours de lecture.")
                else:
                    debug("Aucune note à supprimer car aucune musique en cours de lecture.")
            else:
                debug("Aucune note à supprimer car aucune musique en cours de lecture.")
    


if __name__ == '__main__':
    bot = Bot()
    trigger_fail = False
    while True:
        try:
            bot.update(sp)
            sleep(int(SLEEP_TIME))
        except spotipy.exceptions.SpotifyException as e:
            if e.http_status == 401:
                debug("le jeton à expiré chargement d'un nouveau...")
                access_token = get_access_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REFRESH_TOKEN)
                sp = spotipy.Spotify(auth=access_token)
                debug("le jeton à bien été changé")
            else:
                raise e
