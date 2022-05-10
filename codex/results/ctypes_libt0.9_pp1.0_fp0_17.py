import ctypes
ctypes.cdll.LoadLibrary("/usr/lib/x86_64-linux-gnu/libX11.so")
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
plt.ion()

import gc

try:
    print("Imported numpy")
except:
    print("Failed to import numpy")

try:
    import scipy
    print("Imported scipy")
except:
    print("Failed to import scipy")

try:
    import matplotlib
    print("Imported matplotlib")
except : 
    print("Failed to import matplotlib")

try:
    import sklearn
    print("Import sklearn")
except:
    print("Failed to import sklearn")

try:
    import xgboost
    print("Import xgboost")
except:
    print("Failed to import xgboost")

try
