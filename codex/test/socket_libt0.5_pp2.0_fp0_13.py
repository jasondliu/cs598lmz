import socket
import sys
import threading
import time

from datetime import datetime
from multiprocessing import Process
from random import randint

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# import the serial library
import serial

#import the visa library
import visa

#import the time library
import time

#import the numpy library
import numpy

#import the matplotlib library
import matplotlib.pyplot as plt

#import the PyQt4 modules for all the commands that control the GUI.
from PyQt4.QtCore import *
