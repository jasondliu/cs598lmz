import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("NO NAME's AVIToGIF")


import os
import shutil
import subprocess

from multiprocessing import Process,freeze_support
from subprocess import Popen,PIPE
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter.ttk import *
from tkinter.ttk import Progressbar
from tkinter import Menu,Label,Button,Grid,Scrollbar,Text,Entry,Frame,StringVar,PhotoImage,IntVar
from PIL import Image,ImageTk
from time import sleep

class AVIToGIF(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        self.master.title("AVIToGIF")
        self.master.resizable(True,False)
        self.master.configure(background="#242424")
        self.master.protocol("WM_DELETE_WINDOW",self.client_exit)
        self.master
