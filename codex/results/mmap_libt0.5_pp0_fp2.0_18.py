import mmap
import numpy as np
import time
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal
from scipy.signal import savgol_filter
import os
from scipy.signal import find_peaks
from scipy.signal import peak_widths
from scipy.signal import argrelextrema
from scipy.signal import medfilt
from scipy.signal import wiener
from scipy.signal import medfilt
from scipy.signal import wiener
from scipy.signal import medfilt
from scipy.signal import wiener
from scipy.signal import medfilt
from scipy.signal import wiener
from scipy.signal import medfilt
from scipy.signal import wiener

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
   
