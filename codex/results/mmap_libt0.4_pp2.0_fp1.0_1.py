import mmap
import numpy as np
import struct
import sys
import time
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from scipy.signal import butter, lfilter, firwin

# from scipy.signal import freqz

# from scipy.signal import freqz

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.
