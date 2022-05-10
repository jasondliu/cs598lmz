import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5 import QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np
import sys
import os
import time
import datetime
import threading
import queue
import struct
import math

# local imports
from ui_mainwindow import *
import ui_settingsdialog
import ui_setpointdialog
import ui_aboutdialog
import ui_datadialog
import ui_plotdialog
import ui_saveplotdialog
import ui_savedatadialog
import ui_loaddatadialog
import ui_
