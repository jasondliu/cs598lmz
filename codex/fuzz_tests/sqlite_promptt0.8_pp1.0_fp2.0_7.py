import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

from PyQt5.QtCore import Qt, QSettings, QByteArray, QPoint
from PyQt5.QtGui import QValidator, QDoubleValidator
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QSplitter,
        QWidget, QLabel, QToolTip, QPushButton, QLineEdit, QGridLayout, QComboBox, QAction,
        QTabWidget, QWidget, QTreeWidget,QListWidget, QTextEdit, QMessageBox, QHBoxLayout, QVBoxLayout, QLCDNumber, QGroupBox, QFileDialog, QProgressBar)

import lib_sat

class HvTabWidget(QTabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setParent(parent)
        self.makeWidget()

    def makeWidget(self):
        self.setGeometry(10,10,200,50)
        self.addTab(self,"HV")

        self
