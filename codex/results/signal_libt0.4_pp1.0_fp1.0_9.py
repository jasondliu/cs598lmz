import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import argparse
import logging

import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

import PyQt5
from PyQt5 import QtCore, QtWidgets, QtGui

import pyqtgraph as pg

import pyaudio
import wave

from scipy.io import wavfile

import pyfftw

from pyfftw.interfaces.numpy_fft import fft, ifft, fftshift, ifftshift

import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType

from pyqtgraph.Qt import QtCore, QtGui

from pyqtgraph.dockarea import *

from pyqtgraph.widgets.MatplotlibWidget import Matplotlib
