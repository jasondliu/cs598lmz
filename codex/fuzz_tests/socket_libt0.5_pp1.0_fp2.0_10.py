import socket
import sys
import time
import threading
import tkinter
import tkinter.messagebox
import tkinter.simpledialog

from PIL import Image, ImageTk

class My_chat(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Chat")
        self.geometry("800x600")
        self.resizable(False, False)
        self.iconbitmap("img/chat.ico")

        self.frame_top = tkinter.Frame(self, bg='white', width=800, height=80)
        self.frame_top.pack(side='top')

        self.frame_center = tkinter.Frame(self, bg='white', width=800, height=420)
        self.frame_center.pack(side='top')

        self.frame_bottom = tkinter.Frame(self, bg='white', width=800, height=100)
        self.frame_bottom.pack(side='top')

        self.frame_top
