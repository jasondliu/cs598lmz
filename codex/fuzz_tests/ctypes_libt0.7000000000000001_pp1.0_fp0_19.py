import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread, pyqtSignal
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import os
import sys
import time
import threading
import pywinauto
from pywinauto.application import Application
from pywina
