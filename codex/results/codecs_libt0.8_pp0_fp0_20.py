import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import sys
import os
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import numpy as np
import math
import pandas as pd
from scipy.signal import savgol_filter
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
from scipy.optimize import minimize
from pylab import *
import xlsxwriter
from scipy.signal import savgol_filter
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
from scipy.optimize import minimize
from scipy.signal import find_peaks
from scipy.signal import peak_widths

root = tk.T
