import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os, sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.ptime as ptime
import time
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--datafile', help='data file to read', default='/tmp/data.dat')
parser.add_argument('-l', '--label', help='label for data', default='test')
parser.add_argument('-t', '--test', action='store_true')
parser.add_argument('-d', '--debug', action='store_true')
parser.add_argument('--xmax', help='X max', type=int, default=10)
parser.add_argument('--ymax', help='Y max', type=int, default=10)
args = parser.parse_args()

