import types
types.ModuleType.__repr__ = lambda self: self.__name__

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

import scipy.stats as stats
import scipy.signal as signal
import scipy.interpolate as interp
import scipy.optimize as opt

import astropy.io.fits as fits
import astropy.wcs as wcs
import astropy.units as u
from astropy.coordinates import SkyCoord

import emcee
import corner

import warnings
warnings.filterwarnings('ignore')

import os
import sys
import glob
import time
import datetime
import shutil
import subprocess
import multiprocessing
import pickle
import h5py

from IPython.display import display, Math, Latex

