import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import tkinter as tk

Dpi = 100
LARGE_FONT= ("Verdana", 12)
SMALL_FONT= ("Verdana", 7)

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "GUI")
        tk.Tk.iconbitmap(self, default = 'gui.ico')
        self.geometry("{}x{}".format(Dpi*6,Dpi*2))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(
