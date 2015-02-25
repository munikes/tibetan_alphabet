#    Copyright (C) 2015 mUniKeS
#
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

import os
from random import shuffle
from unicodedata import lookup
from Tkinter import Tk, Button, PhotoImage, Label, Frame
import pygame

TITLE = "Learn Tibetan"
WINDOW_DIMENSIONS = "185x260+100+80"
SOUNDS_PATH = os.path.join(os.path.dirname(__file__), "../sounds/")
IMAGES_PATH = os.path.join(os.path.dirname(__file__), "../images/")

LETTERS = {lookup("tibetan letter ka"):("ka", SOUNDS_PATH + "ka.ogg"),
          lookup("tibetan letter kha"):("k'a", SOUNDS_PATH + "kha.ogg"),
          lookup("tibetan letter ga"):("k_'a", SOUNDS_PATH + "kh_a.ogg"),
          lookup("tibetan letter nga"):("nga", SOUNDS_PATH + "nga.ogg")}

NUM_LETTERS = 4


def shuffle_dictionary (dictionary):
    """
    Return random keys of dictionary
    """
    # Python 3
    # keys =  list(dictionary.keys())
    # Python 2
    keys = dictionary.keys()
    shuffle(keys)
    return keys


def generate_letters(list_letters, NUM_LETTERS):
    """
    Return a right letter and a list of shuffle letters
    """
    right_letter = list_letters[0]
    letters = list_letters[0:NUM_LETTERS]
    shuffle(letters)
    return right_letter, letters


def play_ogg(list_oggs):
    """
    Play a list of oggs
    """
    i=0
    SONG_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load(list_oggs[i])
    pygame.mixer.music.play()

    running = True
    while running:
        for event in pygame.event.get():
            if  i >= len(list_oggs) - 1:
                running = False
            elif event.type == SONG_END:
                pygame.mixer.music.load(list_oggs[i+1])
                pygame.mixer.music.play()
            i+=1


class Application(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent)
        self.parent = parent

        # generate the options of buttons
        keys = shuffle_dictionary(LETTERS)
        right_answer, answers = generate_letters(keys, NUM_LETTERS)
        # create window
        self.create_window()
        self.create_letter(right_answer)
        #self.create_button()
        self.create_play_button(answers)
        self.create_option_buttons(right_answer, answers)

    def create_window (self):

        self.parent.geometry(WINDOW_DIMENSIONS)
        self.parent.title(TITLE)

    def create_letter(self, right_answer):

        self.label = Label(self.parent, text=right_answer, font=("",80))
        self.label.pack()

    def create_button(self):

        self.button = Button().place(x=5,y=102)

    def create_play_button(self, answers):

        # create list of oggs
        list_oggs = []
        i= 0
        for i in range(0, NUM_LETTERS):
            list_oggs.append(LETTERS[answers[i]][1])
            i+=1
        self.play_image = PhotoImage(file=IMAGES_PATH + 'play.png')
        # create the button
        self.play_button = Button(self.parent,width=40,height=30,fg='black',
            image=self.play_image, command=lambda: play_ogg(list_oggs)).place(x=5,y=102)

    def right_button(self, button):
        """
        Button right green and sound
        """
        button.config(background = "green")
        button.config(activebackground="green")
        pygame.mixer.music.load(SOUNDS_PATH + 'right.ogg')
        pygame.mixer.music.play()

    def wrong_button(self, button):
        """
        Button wrong red and sound
        """
        button.config(background = "red")
        button.config(activebackground="red")
        pygame.mixer.music.load(SOUNDS_PATH + 'wrong.ogg')
        pygame.mixer.music.play()

    def create_option_buttons(self, right_answer, answers):

        # create buttons
        self.option_1 = Button(self.parent,width=7,height=3,fg='black',
                  text=LETTERS[answers[0]][0])
        self.option_1.place(x=5,y=140)
        self.option_2 = Button(self.parent,width=7,height=3,fg='black',
                  text=LETTERS[answers[1]][0])
        self.option_2.place(x=5,y=200) 
        self.option_3 = Button(self.parent,width=7,height=3,fg='black',
                  text=LETTERS[answers[2]][0])
        self.option_3.place(x=95,y=140)
        self.option_4 = Button(self.parent,width=7,height=3,fg='black',
                  text=LETTERS[answers[3]][0])
        self.option_4.place(x=95,y=200)
        self.option_1.config(command=lambda:
                             self.right_button(self.option_1) if answers[0] == right_answer
                             else self.wrong_button(self.option_1))
        self.option_2.config(command=lambda:
                             self.parent.right_button(self.option_2) if answers[1] == right_answer
                             else self.wrong_button(self.option_2))
        self.option_3.config(command=lambda:
                             self.right_button(self.option_3) if answers[2] == right_answer
                             else self.wrong_button(self.option_3))
        self.option_4.config(command=lambda:
                             self.right_button(self.option_4) if answers[3] == right_answer
                             else self.wrong_button(self.option_4))


def main():

    pygame.init()
    root = Tk()
    app = Application(root)
    root.mainloop()
    pygame.quit()


if __name__ == '__main__':
    main()
