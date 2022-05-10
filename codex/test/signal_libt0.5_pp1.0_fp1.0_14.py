import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton, QComboBox, QCheckBox, QLineEdit, QStackedWidget, QTabWidget, QTreeWidget, QTreeWidgetItem, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

import sys
import os
import json
from collections import OrderedDict
from datetime import datetime
from datetime import timedelta

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
