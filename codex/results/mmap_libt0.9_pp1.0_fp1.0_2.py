import mmap
from _winreg import *
from Tkinter import *
from tkMessageBox import *
from Frame import *
import time
from PIL import ImageTk
from PIL import Image

class App(Frame):
    """
    Class for controlling the application
    """
    def __init__(self,master=None):
        """
        Initializes the frame using Frame class
        If an error pops up from the Frame class, then the program will close
        """
        Frame.__init__(self,master)
        self.pack()
        if self.Error:
            self.quit()

        
        self.error = False
        self.root = master
        self.create()
        self.buttonDict = {}
        self.rDict = {}
        self.eDict = {}
        self.addButtons()
        self.data = "3c3c3c3c3c3c00000010000000010000000000800000000003d000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

        
        self.rVar = IntVar()
        self.rVar.set
