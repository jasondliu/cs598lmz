import mmap
import struct
import os
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import json

def fft(signal, fs):
	# Number of samplepoints
    N = len(signal)

    # length of signal
    T = 1.0 / fs
    x = np.linspace(0.0, N*T, N)
    y = signal
    yf = np.fft.rfft(y)
    #print(yf)
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
    return (xf, np.abs(yf[:int(N/2)]))

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff,
