import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import random
import time

from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtGui import QFont

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QLineEdit, QLabel
from PyQt5.QtCore import Qt

from name_generator import name_generator

from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5.Qt
