import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Progressbar

from tkinter.filedialog import asksaveasfilename
from PIL import ImageTk, Image

from netCDF4 import Dataset
import numpy as np
import numpy.ma as ma
from numpy import genfromtxt
import matplotlib.pyplot as plt

import pandas as pd
import os
import sys
import time
from datetime import datetime
from datetime import timedelta

from SeaIceDataExtractor import *

import time


# ##############################
# Setting up the user interface
# ##############################

#Start the GUI
root = Tk()
root.title("Sea Ice Analysis Tool");

#Default display size
root.geometry("800x600")

#Set the default font
font
