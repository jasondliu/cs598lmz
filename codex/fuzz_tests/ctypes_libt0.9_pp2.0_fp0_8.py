import ctypes
ctypes.windll.shcore.SetProcessDPIAware()
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

def addApp():
	filename = filedialog.askopenfilename(initialdir="/", title="Select File",
		filetypes=(("executables","*.exe"),("all files","*.*")) )
	
	apps.append(filename)

	print(apps)
	for app in apps:
		label = tk.Label(frame,text=app,bg="gray")
		label.pack()

def runApps():
	for app in apps:
		os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8, rely=0.1, relx=0.1)

openFile
