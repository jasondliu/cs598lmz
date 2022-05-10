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
