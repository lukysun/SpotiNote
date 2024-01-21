
# SpotiNote 
## Fork de Notify

Si tu à envie d'ajouté du fun à tes note instagram SpotiNote est là pour toi ! 

## Installation

Instalation de SpotiNote
### Depuis GitHub
```bash
  git clone https://github.com/lukysun/SpotiNote.git
  cd SpotiNote
```
### Par Ficher .zip
clique sur le bouton "code" puis télécharger le .zip
puis l'extraire dans un dossier comme toute autre zip !
ouvrir un terminal/cmd dans le dossier
![image](https://github.com/lukysun/SpotiNote/assets/90115054/619cb0cf-0013-4bf8-ad12-bda0949fdc37)

### télécharge les dépendence et lance le script

```bash
  pip install -r requirements.txt
  python spotinote.py
```
    
## Environment Variables

pour utilisé ce script tu dois entrer tes variables lors du 1er lançement de l'application tu trouveras le tout ici : https://developer.spotify.com/dashboard 

### étape : 
- sur le site https://developer.spotify.com/dashboard clique sur "create app" puis crée en une
![image](https://github.com/lukysun/SpotiNote/assets/90115054/7542d4c0-913c-44a0-a867-57e7f3b9ec79)

- une fois l'application crée clique sur "setting"
![image](https://github.com/lukysun/SpotiNote/assets/90115054/ea72806a-5127-4e1d-8340-441309099f23)

`SPOTIPY_CLIENT_ID`:
*L'id de ton bot spotify trouvable ici : 
![image](https://github.com/lukysun/SpotiNote/assets/90115054/d154a6a5-525f-48ce-a10b-096f5f5b8b09)


`SPOTIPY_CLIENT_SECRET`:
*Ttout d'abord cclique sur "client secret" *puis copie la clé qui s'affiche*
![image](https://github.com/lukysun/SpotiNote/assets/90115054/8ad50c98-3877-47ac-af3e-788c1076a724)
*
`SPOTIPY_REFRESH_TOKEN`:
*le jeton sert à se connecté à spotify tu peux le trouvé comme ceci : *
-d'abord tu vas te rendre sur le site : https://spotify-refresh-token-generator.netlify.app et cliqué sur le bouton "get started"
![image](https://github.com/lukysun/SpotiNote/assets/90115054/4b9b4962-dafe-4a7b-82f6-14cdfe44ec16)

-puis tu clique sur "Already got the required data? Skip this step"
![image](https://github.com/lukysun/SpotiNote/assets/90115054/9a057e9e-472d-4253-94b9-0118e08e2b9b)
pour continuer tu vas retourner sur : https://developer.spotify.com/dashboard puis sur ton app et dans les parmètre (voir les 2 premières étape)
et dans "redirect url tu vas rentré ceci : https://spotify-refresh-token-generator.netlify.app
tu vas entré les information que tu à récupéré précédament comme ceci : 
![image](https://github.com/lukysun/SpotiNote/assets/90115054/6600d937-a557-4b21-90c7-1a32b3bc8dde)

![image](https://github.com/lukysun/SpotiNote/assets/90115054/de9ff05f-3574-43fc-a1aa-a711179f8204)
-ensuite tu clique sur "tout les scope" et clique sur le bouton "get spotify acces code"
![image](https://github.com/lukysun/SpotiNote/assets/90115054/290966e2-fae8-4716-a009-9c15401c46e3)
- et voilà tu a juste à copier ton jeton ! 

`BOT_REFRESH_RATE`:
*Ceci est le temps que le bot vas mettre avant de mettre à jour la note instgram*  
# 🛑 je déconseille fortement de mettre en dessous de 150 seconde sous peine de trigger l'api de instgram !

POUR CE QUI SUIT, LA SUITE DES MOT DANS LA NOTE EST DEFINIE PAR : 
<préfix> (titre) <séparateur> <artiste>
`SONG_SEPARATOR`:
*ceci est le mot ou le symbole qui sera entre m'artiste et le litre *
vour pouvez ajouté un mot comme "de" ou "par" si je prend l'exemple de la musique alone de alan walker et que je choisit le séparateur "de" alord j'aurais dans ma note :
"alone de alan walker"
mais si je choisit "par" alors j'aurais : 
"alone par alan walker"
`préfix`
celui si est un texte se trouvant au début de la note 
## 🚫 ATTENTION EVITE DE METTRE UN TROP LONG PRÉFIXE CAR UNE NOTE EST LIMITÉ à 60 CARACTERE !
`IG_USERNAME`
*ton pseudo instagram*

`IG_PASSWORD`
*Ton mot de passe instagram*



## FAQ

# A VENIR
