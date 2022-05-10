import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import style
style.use("ggplot")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import matplotlib.animation as animation
from matplotlib import style

import urllib
import json

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)

# returns a dataframe containing the stock prices of the stock symbol passed in
def getStockData(symbol):
	url = "http://www.google.com/finance/historical?output=csv&q=" + symbol
	sourceCode = urllib.request.urlopen(url).read().dec
