import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import os
import time
import datetime
import threading

import numpy as np

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator

from ui_main import Ui_MainWindow
from ui_about import Ui_AboutDialog
from ui_error import Ui_ErrorDialog
from ui_help import Ui_HelpDialog
from ui_settings import Ui_SettingsDialog
from ui_settings_plot import Ui_SettingsPlotDialog
from ui_settings_measure import U
