import ctypes
import ctypes.util
import threading
import sqlite3
import os

from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QThread, QSize, QPoint
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QGroupBox, QCheckBox, QApplication, QComboBox, QMessageBox, QProgressBar, QFileDialog, QDesktopWidget, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap

import ui_mainwindow

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory
