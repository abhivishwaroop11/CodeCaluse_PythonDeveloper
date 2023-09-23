import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3

root = Tk()
root.minsize(500, 500)

ListOfSongs = []
realNames = []

v = StringVar()
SongLabel = Label(root, textvariable=v, width=100)

index = 0


def directoryChooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            Real_dir = os.path.realpath(files)
            audio = ID3(Real_dir)
            realNames.append(audio['TIT2'].text[0])

            ListOfSongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(ListOfSongs[0])
    pygame.mixer.music.play()


directoryChooser()


def UpdateLabel():
    global index
    global songname
    v.set(realNames[index])


def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(ListOfSongs[index])
    pygame.mixer.music.play()
    UpdateLabel()


def Prev_song(event):
    global index
    index -= 1
    pygame.mixer.music.load(ListOfSongs[index])
    pygame.mixer.music.play()
    UpdateLabel()


def Unpause_song(event):
    pygame.mixer.music.unpause()
    # pause button.config(text="pause song")
    v.set("Song unpause")


def Pause_song(event):
    pygame.mixer.music.pause()
    v.set("Song Paused")


def Stop_song(event):
    pygame.mixer.music.stop()
    v.set("")


label = Label(root, text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()


realNames.reverse()

for items in realNames:
    listbox.insert(0, items)

realNames.reverse()


next_button = Button(root, text='Next Song')
next_button.pack()

previous_button = Button(root, text='Previous Song')
previous_button.pack()

pause_button = Button(root, text='Pause Song')
pause_button.pack()

unpause_button = Button(root, text='Unpause Song')
unpause_button.pack()

stop_button = Button(root, text='Stop Music')
stop_button.pack()

next_button.bind("<Button-1>", nextsong)
previous_button.bind("<Button-1>", Prev_song)
pause_button.bind("<Button-1>", Pause_song)
unpause_button.bind("<Button-1>", Unpause_song)
stop_button.bind("<Button-1>", Stop_song)

SongLabel.pack()
root.mainloop()
