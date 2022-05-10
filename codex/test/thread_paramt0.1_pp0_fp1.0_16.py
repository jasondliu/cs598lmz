import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

import time

import pyaudio
import wave

import scipy.io.wavfile as wav

import scipy.signal as sig

import scipy.fftpack as fft

import os

import math

import random

import csv

import pandas as pd

import scipy.stats as stats

import scipy.optimize as opt

import scipy.integrate as integrate

import scipy.special as special

import scipy.interpolate as interpolate

import scipy.spatial as spatial

import scipy.cluster as cluster

import scipy.ndimage as ndimage

import scipy.fftpack as fftpack

