import ctypes
ctypes.cdll.LoadLibrary('libquadprog.so')
ctypes.cdll.LoadLibrary('libmosek64.so')

# Imports Modules for the Rest of the Program
import numpy as np
import pandas as pd
import math
import datetime as dt
from tia.bbg import LocalTerminal
from scipy.stats import norm
from openpyxl import load_workbook

# Imports the Portfolio Functions
import Quadratic_Programming_Functions as port

# Imports the Window
import Tkinter, tkFileDialog

pd.options.mode.chained_assignment = None

def risk_management_tool():
    '''
    This is the Risk Management Tool used to figure out the best portfolio.
    It is iterative, running many Monte Carlo analysis to find the best
    weights.
    '''

    root = Tkinter.Tk()
    root.withdraw()
    file_path = tkFileDialog.askopenfilename()

    wb = load_workbook(file_path)
    sheet
