import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QFont, QPixmap, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QDialog, QSplashScreen, QLabel
from PyQt5.QtCore import QCoreApplication, Qt, QThread, QSize

from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

import threading
import time
import sys

import serial
import serial.
