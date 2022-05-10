import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QTextEdit, QDesktopWidget, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, Qt, QThread, pyqtSignal
from PyQt5 import QtCore

import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class EmittingStream(QtCore.QObject):
    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


class Window(QWidget):

    def __init__(self):
        super().__init__()
