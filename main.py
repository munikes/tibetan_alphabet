#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from random import shuffle
from unicodedata import lookup
from Tkinter import *
from pygame import mixer
from tkSnack import *

letras = {lookup("tibetan letter ka"):("ka", "sound/ka.mp3"), 
          lookup("tibetan letter kha"):("k'a", "sound/kha.mp3"),
          lookup("tibetan letter ga"):("k_'a", "sound/kh_a.mp3"),
          lookup("tibetan letter nga"):("nga", "sound/nga.mp3")}

# return random keys 
def shuffle_dictionary (dictionary):
    # Python 3 
    # keys =  list(dictionary.keys())
    # Python 2 
    keys = dictionary.keys()
    shuffle(keys)
    return keys
        
def generate_question(list_questions):
    right_answer = list_questions[0]
    answers = list_questions[0:4]
    shuffle(answers)
    return right_answer, answers

def play_ogg():
    mixer.init()
    mixer.music.load('Example.ogg')
    mixer.music.play()
    
#print letras["ka"][0] # letra tibetana (importante poner el print)
#letras["ka"][1] # fichero de sonido

# random the letters
keys = shuffle_dictionary(letras)
right_answer, answers = generate_question(keys)
ventana = Tk()
initializeSnack(ventana)
ventana.geometry("185x260+100+80")
label = Label(ventana, text = right_answer, font=("", 80))
label.pack()

play_sound=Button(ventana,width=40,height=30,fg='black',
            bitmap='snackPlay', command=play_ogg).place(x=5,y=102)
option_1 = Button(ventana,width=7,height=3,fg='black', 
                  text=letras[answers[0]][0]).place(x=5,y=140) 
option_2 = Button(ventana,width=7,height=3,fg='black', 
                  text=letras[answers[1]][0]).place(x=5,y=200) 
option_3 = Button(ventana,width=7,height=3,fg='black', 
                  text=letras[answers[2]][0]).place(x=95,y=140)
option_4 = Button(ventana,width=7,height=3,fg='black', 
                  text=letras[answers[3]][0]).place(x=95,y=200)

ventana.mainloop()