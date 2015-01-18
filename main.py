from random import shuffle
from unicodedata import lookup
from Tkinter import *
from pygame import mixer

letras = {lookup("tibetan letter ka"):("ka", "sound/ka.mp3"), 
          lookup("tibetan letter kha"):("k'a", "sound/kha.mp3"),
          lookup("tibetan letter ga"):("k'a", "sound/kh_a.mp3"),
          lookup("tibetan letter nga"):("nga", "sound/nga.mp3")}

def generate_question(list_questions):
    shuffle(list_questions)
    right_answer = list_questions[0]
    wrong_answers = [list_questions[1],list_questions[2],
                     list_questions[3]]
    return right_answer, wrong_answers

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
option_2 = Button(ventana,width=50,height=50,fg='black', 
            bitmap='snackStop').place(x=60,y=501) 
option_3 = Button(ventana,width=50,height=50,fg='black', 
                bitmap='snackPlay', command=play_ogg).place(x=115,y=501) 
option_4 = Button(ventana,width=5,height=3,fg='black', 
                text='Save').place(x=170,y=501) 
ventana.mainloop()