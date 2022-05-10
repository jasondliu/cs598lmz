import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

from scipy.signal import chirp, find_peaks, peak_prominences, peak_widths, savgol_filter
from scipy.optimize import curve_fit
from scipy.special import erfc

import os
import sys
import glob

import pandas as pd

from datetime import datetime

from scipy.stats import norm
from scipy.optimize import curve_fit

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from tqdm import tqdm

import peakutils

import matplotlib.gridspec as gridspec

from matplotlib.colors import LogNorm

import matplotlib.patches as patches

from matplotlib.widgets import RectangleSelector

from PIL import Image

from scipy.optim
