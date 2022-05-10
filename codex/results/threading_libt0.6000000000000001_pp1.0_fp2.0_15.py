import threading
threading.stack_size(2**27)
import sys
import argparse
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pyqtgraph.ptime as ptime
from collections import deque
from pyqtgraph.dockarea import *

# initialize
pg.setConfigOptions(antialias=True)

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="serial port to listen on")
parser.add_argument("-b", "--baudrate", help="serial port baudrate")
parser.add_argument("-c", "--columns", help="number of columns")
parser.add_argument("-r", "--rows", help="number of rows")
parser.add_argument("-f", "--framerate", help="framerate")
parser.add_argument("-g", "--gain", help="gain")
parser.add_argument("-o", "--offset", help="offset")
parser.add
