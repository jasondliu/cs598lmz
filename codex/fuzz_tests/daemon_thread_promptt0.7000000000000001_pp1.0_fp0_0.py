import threading
# Test threading daemon

# import pandas as pd
# from pandas import DataFrame, Series

import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib import mlab

from matplotlib.ticker import FormatStrFormatter

# from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY, date2num
import matplotlib.dates as mdates

from mpl_finance import candlestick_ohlc

import tkinter as tk
from tkinter import ttk, filedialog

from tkinter import *
from tkinter.ttk import *

import os

def getdata(d,p):
    if (d[p][0] == 'D'):
