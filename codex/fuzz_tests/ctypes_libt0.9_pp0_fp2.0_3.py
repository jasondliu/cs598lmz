import ctypes
ctypes.cdll.LoadLibrary("libmkl_rt.so")
from multiprocessing import Pool
import functools
from math import log10
import scipy
from scipy import signal
import struct
import decimal
from decimal import *
import matplotlib.pyplot as plt
getcontext().prec = 400
import pandas as pd
import xarray as xr
from dask.distributed import Client
import dask.dataframe as dd
client = Client()
client

from ipywidgets import IntProgress
from IPython.display import display, clear_output
import time

from scipy.signal import butter, lfilter, freqz
A4 = 440
C0 = A4*pow(2, -4.75)
name = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
def pitch(freq):
    h = round(12*log10(float(freq)/C0)/log10(2))

