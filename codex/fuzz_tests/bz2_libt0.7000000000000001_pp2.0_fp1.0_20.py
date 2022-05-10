import bz2
bz2.BZ2Compressor()

# http://stackoverflow.com/questions/27732354/matplotlib-animation-in-tkinter-canvas
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# http://stackoverflow.com/questions/14541763/how-to-move-a-tkinter-window-using-the-mouse
import ctypes
user32 = ctypes.windll.user32

# http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
import tkinter as tk
from tkinter import ttk

import pickle
from datetime import datetime
from datetime import timedelta
import os
import glob
import time

from gui import gui
from gui import gui_2
from gui import gui_3
from gui import gui_4
from gui import gui_5
from gui import gui_6

