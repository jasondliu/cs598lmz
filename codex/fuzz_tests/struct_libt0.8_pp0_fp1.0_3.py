import _struct
import math
import numpy as np

from ex import ex
from r2d2 import r2d2
from wezel import Wezel

from scipy.signal import butter, lfilter, freqz, filtfilt
from sklearn.linear_model import LinearRegression

from scipy import signal

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='bandpass')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_lowpass(highcut, fs, order=6):
    nyq = 0.5 * fs
    high = highcut / nyq
