import threading
threading.stack_size(67108864) # 64MB stack

#======================
# imports
#======================
import sys
import time
import random
#import os
#import inspect
import ctypes
import math
import pdb
import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
#import matplotlib.ticker as ticker
import numpy as np
import glob
import argparse
import traceback
import subprocess

from mpl_toolkits.mplot3d import Axes3D
from pylab import *
from numpy import *
from numpy import linalg
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui


#======================
# defines
#======================
#define the threshold of points to be considered as a line
THRESHOLD_NUM_OF_POINTS=1
#define the threshold of error to be considered as a line
THRESHOLD_ERROR=4
#define the threshold of error to be stop fitting
