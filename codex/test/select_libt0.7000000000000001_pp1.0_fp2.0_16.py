import select
import socket
import sys
import threading
import time
from threading import Thread
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

# Define some global variables
HOST = '127.0.0.1'  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port
url = ''
timeout = 10

class MyClient(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(expand = YES, fill = BOTH)
        self.master.title('Client')
       
