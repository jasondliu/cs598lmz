import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
from PIL import Image
from PIL import ImageTk
import tkinter as tk
import pandas as pd

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.configure(background='gray80')
       label = tk.Label(self, text="This is page 1", bg="gray80")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.configure(background='gray80')
       label =
