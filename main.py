from random import shuffle
from unicodedata import lookup

letras = {"ka":(lookup("tibetan letter ka"), "sound/ka.mp3"), 
          "kha":(lookup("tibetan letter kha"), "sound/kha.mp3")}

print letras["ka"][0] # letra tibetana (importante poner el print)
letras["ka"][1] # fichero de sonido