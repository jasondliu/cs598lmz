import mmap
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

X_ENCODER_TO_INCHES_FACTOR = 1
Y_ENCODER_TO_INCHES_FACTOR = 1
X_ENCODER_TO_MM_FACTOR = 25.4
Y_ENCODER_TO_MM_FACTOR = 25.4

# this is a test comment

class App():

    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.canvas = tk.Canvas(self.root, width=1920, height=1080)
        self.canvas.pack()
        self.background_image = tk.PhotoImage(file = "background.gif")
        self.w = self.background_image.width()
        self.h = self.background_image.height()
        # self.canvas.create_image(0, 0, anchor=tk.NW, image
