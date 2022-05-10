import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
import cv2
import numpy as np
import sys

# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.uic import loadUi
# import cv2
# import numpy as np
# import sys


