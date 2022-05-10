import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Remote_Control")

import socket
import threading
import os
import sys
import subprocess
import pyautogui
import cv2
import numpy as np
import time
import dlib
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QMainWindow, QLineEdit,
                             QHBoxLayout, QVBoxLayout, QGroupBox, QAction, QFileDialog, QMessageBox,
                             QProgressBar, QComboBox, QTextEdit)
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTextCursor
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal, Qt
from sklearn.externals import joblib
from PIL import ImageGrab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tw = None
        self.initUI()

    def initUI(self):

