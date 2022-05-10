import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QListWidget, QHBoxLayout, QLineEdit, QAction, QFileDialog, QLabel, QGridLayout, QStyle, QToolBar, \
    QListWidgetItem, QCheckBox, QFormLayout, QGroupBox, QSpinBox, QDoubleSpinBox, QShortcut
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont, QColor, QKeySequence
from PyQt5.QtCore import pyqtSlot, Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib
import numpy
