import select
import os, sys, time
from math import ceil
import subprocess
from threading import Thread
import ctypes

#python setup.py build_ext --inplace

#import numpy as np
from numpy import concatenate
from numpy import interp
from scipy.io.wavfile import read
from scipy.signal import freqz
from scipy.signal import butter, filtfilt
from scipy import signal
from scipy.fftpack import fft
from scipy import fftpack
from scipy import ndimage, stats
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from ttkthemes import themed_tk as tk
from PIL import ImageTk, Image
from winsound import Beep

from key_gestures import *
from graphing import *
from continuous_timedomain import *
from continuous_frequencydomain import *
from vad import *

from ctypes import
