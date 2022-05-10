import mmap
import sys
import time
import datetime
import math

from collections import deque

from multiprocessing import Process, Queue

import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

import pyaudio

from scipy import signal

from scipy.fftpack import fft

import scipy.io.wavfile as wav

from scipy.signal import butter, lfilter

from scipy.signal import freqz

from scipy.signal import hilbert

