import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os
from scipy.io import wavfile
from scipy.signal import butter, lfilter
from scipy.fftpack import fft, ifft, fftfreq
from scipy.signal import hilbert
from scipy.signal import freqz
from scipy.signal import correlate
from scipy.signal import decimate
from scipy.signal import find_peaks
from scipy.signal import peak_widths
from scipy.signal import savgol_filter
from scipy.signal import medfilt
from scipy.signal import wiener
from scipy.signal import filtfilt
from scipy.signal import butter, lfilter, freqz
from scipy.signal import resample
from scipy.signal import argrelextrema
from scipy.sign
