import codecs
codecs.register_error('strict', codecs.ignore_errors)

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = ttk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=0, column=0)

        self.quit = ttk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=1, column=0)

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk
