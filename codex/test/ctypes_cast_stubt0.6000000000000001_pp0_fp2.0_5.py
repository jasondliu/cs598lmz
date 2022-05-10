import ctypes
ctypes.cast(4, ctypes.py_object)

#clear all variables
def clearall():
    all = [var for var in globals() if var[0] != "_"]
    for var in all:
        del globals()[var]

#reset -f
clearall()

#import libraries
import numpy as np
import pandas as pd
