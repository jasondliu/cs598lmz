import ctypes
import ctypes.util
import threading
import sqlite3

from sys import platform
from os import path
from datetime import datetime
from time import sleep
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMessageBox, QProgressBar, QFileDialog,
                             QDialog, QListWidget, QListWidgetItem, QComboBox, QSpinBox, QCheckBox, QMenu)
from PyQt5.QtCore import Qt, QObject, QTimer, pyqtSignal, pyqtSlot, QThread, QDate, QDateTime
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QCursor
from PyQt5.Qt import *


class MySignal(QObject):
    '''自定义信号类'''
    my_signal = pyqtSignal(str)



