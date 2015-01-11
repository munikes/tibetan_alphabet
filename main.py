from random import shuffle
from unicodedata import lookup
from Tkinter import *
from pygame import mixer

letras = {"ka":(lookup("tibetan letter ka"), "sound/ka.mp3"), 
          "kha":(lookup("tibetan letter kha"), "sound/kha.mp3")}

def play_ogg():
    mixer.init()
    mixer.music.load('Example.ogg')
    mixer.music.play()
    
#print letras["ka"][0] # letra tibetana (importante poner el print)
#letras["ka"][1] # fichero de sonido

ventana = Tk()
ventana.geometry("650x560+100+80")
label = Label(ventana, text = letras['ka'][0], font=("", 80))
label.pack()
#play_sound=Button(ventana,width=50,height=50,fg='black',
#            bitmap='snackPlay', command=play_ogg).place(x=115,y=501)
option_1 = Button(ventana,width=50,height=50,fg='red', 
                  bitmap='snackRecord').place(x=5,y=501) 
option_2=Button(ventana,width=50,height=50,fg='black', 
            bitmap='snackStop').place(x=60,y=501) 
option_3=Button(ventana,width=50,height=50,fg='black', 
                bitmap='snackPlay', command=play_ogg).place(x=115,y=501) 
option_4=Button(ventana,width=5,height=3,fg='black', 
                text='Save').place(x=170,y=501) 
ventana.mainloop()