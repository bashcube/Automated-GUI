from tkinter import *
from tkinter import font
import os

GIT_REPO = "https://github.com/<Your repo>/" # link to your git repo
GMAIL_ACC = "https://gmail.com" # password saved in the keychain of browser.
SONG_LIST = "/$USER/Music/" # path for music playlist directory

def opengit():
	os.system("firefox --new-window -url "+GIT_REPO)

def openmail():
	os.system("firefox --new-window -url "+GMAIL_ACC)

def playsongs():
	os.system("mpg123 -z -vC "+SONG_LIST+"*.mp3")

def Continue():
	return ''

def main():
	window = Tk()
	window.geometry("300x230")
	window.title("Automating Tasks...")

	fonts = font.Font(family='Helvetica', size=11, weight='bold')

	Frame1 = LabelFrame(window, text="TASK 1.")
	Frame1.pack(fill="both", expand="yes")

	btn1 = Button(Frame1, text = 'OPEN GIT REPOSITORY',font = fonts, command = opengit, height = 2, width = 33)
	btn1.place(x = 0, y = 0)

	Frame2 = LabelFrame(window, text = "TASK 2.")
	Frame2.pack(fill="both", expand = "yes")

	btn1 = Button(Frame2, text = 'OPEN GMAIL ACCOUNT',font = fonts, command = openmail,height = 2, width = 33)
	btn1.place( x = 0, y = 0)

	Frame3 = LabelFrame(window, text = "TASK 3.")
	Frame3.pack(fill="both", expand = "yes")

	btn1 = Button(Frame3, text = 'PLAY MUSIC ', font = fonts, command = playsongs, height = 2, width = 33)
	btn1.place( x = 0, y = 0)

	window.mainloop()

main()
