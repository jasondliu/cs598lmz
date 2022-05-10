import mmap
import numpy as np
import time
import os
import sys
#from scipy.optimize import curve_fit
#from scipy.interpolate import interp1d

#folder = "../../../data/raw_data/8-29-19-data/new_data/"
#folder = "../../../data/raw_data/8-29-19-data/new_data/"
folder = "../../../data/raw_data/8-29-19-data/new_data/after_hardware_fixes/"

#folder = "../../../data/raw_data/8-29-19-data/new_data/after_hardware_fixes/"
#folder = "../../../data/raw_data/8-29-19-data/new_data/after_hardware_fixes/after_hardware_fixes/"

filenames = [
    "0000",
    "0001",
    "0002",
    "0003",
    "0004",
    "0005",
    "0006",
    "0007",

