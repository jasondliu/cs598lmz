import _struct
from serial.tools import list_ports
from struct import unpack
import threading
from time import sleep
import time
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.filedialog import askopenfilenames, asksaveasfilename
import traceback

from . import Impedance_GUI
import numpy as np

# define GUI
class Impedance_Measurement(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title("Impedance Measurement")
        self.master.geometry('600x400')
        self.master.resizable(0, 0)
        
        self.I_label = ttk.Label(self, text="I")
        self.I_label.grid(row=0, column=0, padx=5, pady=5)
