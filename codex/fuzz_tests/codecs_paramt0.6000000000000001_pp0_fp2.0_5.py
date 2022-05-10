import codecs
codecs.register_error('ignore', codecs.ignore_errors)

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.lines as mlines
import matplotlib.patheffects as PathEffects
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

from matplotlib.colors import LinearSegmentedColormap

import scipy.io as sio
import numpy as np
import os
import glob
import warnings
import sys

warnings.filterwarnings("ignore")

def get_font(font_name):
    return fm.FontProperties(family=font_name)

def get_font_path(font_name):
    font_prop = get_font(font_name)
    font_path = font_prop.get_file()
    return font_path

def get_font_size(font_size):
    return font_size

def get_font_weight(font_weight):
    return font_weight

def get_font_family
