import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patches as mpatches
from matplotlib.widgets import Slider, Button
from matplotlib.ticker import FuncFormatter
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import AnchoredText

from scipy.integrate import odeint
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d

from sklearn.decomposition import PCA

import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import os
import sys
import datetime
import time
import json
import requests
import urllib.request
from bs4 import BeautifulSoup
from tqdm import tqdm

import warnings
warnings.filterwarnings('ignore')


