import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

import time

import pyaudio
import wave

import scipy.io.wavfile as wavfile

import os

import math

from scipy.signal import butter, lfilter

from scipy.fftpack import fft

from scipy.signal import freqz

from scipy.signal import find_peaks

from scipy.signal import correlate

from scipy.signal import hilbert

from scipy.signal import chirp

from scipy.signal import spectrogram

from scipy.signal import resample

from scipy.signal import decimate

from scipy.signal import savgol_filter

from scipy.signal
