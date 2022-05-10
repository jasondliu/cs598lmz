import _struct
from math import *
import numpy as np
from time import time

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from pop_up_windows import AddDataWindow, ChooseDatasetWindow
from gui_utils import *
from gui_main import Ui_MainWindow
from gui_new_dataset import Ui_Dialog
from gui_add_data import Ui_Dialog as Ui_Add_Data

from classes import *
import globals

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.widgets import Button

from data_manipulation import get_data


################################################################################
#                                GUI Main Window                               #
################################################################################


