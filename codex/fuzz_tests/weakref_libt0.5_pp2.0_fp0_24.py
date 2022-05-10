import weakref
import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSizePolicy, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt, QTimer, QEvent
from PyQt5.QtGui import QPixmap, QImage, QTextCursor

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import serial
import serial.tools.list_ports

import time

# from PyQt5.QtWidgets import QWidget,
