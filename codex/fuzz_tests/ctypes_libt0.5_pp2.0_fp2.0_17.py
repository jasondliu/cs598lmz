import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import csv
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.widgets import Button
from scipy import stats
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
from scipy.signal import find_peaks
from scipy.signal import peak_widths
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import curve_fit
from scipy.interpolate import splrep
from scipy.interpolate import splev
from scipy.optimize import minimize
from scipy.optimize import basinhopping
from scipy.optimize import differential_evolution
from scipy.optimize import least_squares
import pandas as pd
from scipy.interpolate import interp
