import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import os
import sys
import re

# Local imports
import datetime

# Data
import glob
import numpy as np
import scipy.interpolate
import scipy.integrate
import scipy.signal
import scipy.stats
import astropy.io.fits
import astropy.stats
import astropy.wcs

import scipy.linalg

# Plotting
import matplotlib.pyplot as pl

# Debugging
import lldb

#%% Constants and utility functions

def stop(): sys.exit()

def get_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

# Paths to data
path_to_data = os.path.join(os.path.dirname(__file__), "data")
path_to_defect_catalog = get_path("data/defect_catalog.fits")
path_to_instrument_spec_table = get_path("data/instrument_spec_table.
