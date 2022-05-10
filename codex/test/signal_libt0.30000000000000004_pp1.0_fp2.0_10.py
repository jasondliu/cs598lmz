import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.patches as patches
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout, QComboBox, QCheckBox, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt, QTimer
