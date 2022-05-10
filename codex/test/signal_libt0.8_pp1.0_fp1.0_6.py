import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import pandas as pd
import numpy as np

import time
import datetime
import sys
import os.path
import math

import multiprocessing as mp
import psutil
import logging
import logging.handlers
import argparse

import binascii

#-----------------------------------------------------------------------------#
#                                                                             #
#                                  Logger                                     #
#                                                                             #
#-----------------------------------------------------------------------------#
LOG_FILENAME = 'datalogger.log'
LOG_LEVEL = logging.INFO  # Could be e.g. "DEBUG
