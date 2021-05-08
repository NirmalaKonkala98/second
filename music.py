# Importing Required Modules & libraries
import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    # Loading Selected Song
    currentsong=playlist.get(ACTIVE)
    # Displaying Selected Song title
    print(currentsong)
     
    mixer.music.load(currentsong)
    # Displaying Status
    songstatus.set("Playing")
    # Playing Selected Song
    mixer.music.play()

def pausesong():
    # Displaying Status
    songstatus.set("Paused")
    #pause song
    mixer.music.pause()

def stopsong():
    # Displaying Status
    songstatus.set("Stopped")
    # Stopped Song
    mixer.music.stop()

def resumesong():
    # Displaying Status
    songstatus.set("Resuming")
    #resume song
    mixer.music.unpause()


# In order to create an empty window
# Passing Root to MusicPlayer Class
root=Tk()
root.title('Music player project')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist---------------
# Inserting Playlist listbox

playlist=Listbox(root,selectmode=SINGLE,bg="Lightgreen",fg="white",font=('arial',20),width=70)
playlist.grid(columnspan=5)
# Creating Playlist Frame
os.chdir(r'C:\Users\lenovo\Desktop\MyPlaylist')
songs=os.listdir()
for s in songs:
    
    playlist.insert(END,s)
# Inserting Play Button
playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('arial',20),bg="Pink",fg="White",padx=7,pady=7)
playbtn.grid(row=1,column=0)
# Inserting Pause Button
pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="Red",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)
# Inserting Stop Button
stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="Blue",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)
# Inserting resume  Button
Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',20),bg="Orange",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()
