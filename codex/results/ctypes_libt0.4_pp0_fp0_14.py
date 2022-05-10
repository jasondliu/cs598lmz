import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#%%
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:46:58 2019

@author: jzhao
"""
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import tkinter.filedialog
import ctypes
import os
import pandas as pd
import numpy as np
import datetime
import time
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as ticker
from matplotlib.figure import Figure
from matplotlib.ticker import ScalarFormatter
import matplotlib.dates as mdates


#%%
class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
