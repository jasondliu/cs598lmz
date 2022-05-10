import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\john\OneDrive\Pictures\Galaxies\HD16029_Cropped.bmp", 0)
 
from PIL import Image

from datetime import date
from datetime import time
from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk, Image

from ttkthemes import ThemedTk
root = ThemedTk()
root.set_theme("vista")

#IMAGE STUFF
img = ImageTk.PhotoImage(Image.open(r"C:\Users\john\OneDrive\Pictures\Galaxies\HD16029_Cropped.bmp"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


#GUI
root.title("Project Genesis Revamped")
root.geometry("600x600")
root.overr
