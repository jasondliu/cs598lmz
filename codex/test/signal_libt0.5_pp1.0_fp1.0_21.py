import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QFrame, QMessageBox, QFileDialog, QProgressBar, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtCore import QThread, pyqtSignal

from PyQt5 import QtCore
import PyQt5.sip

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

import sys
import os
import subprocess
import time

