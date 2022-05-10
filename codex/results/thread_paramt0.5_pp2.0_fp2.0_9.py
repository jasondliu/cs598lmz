import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QComboBox, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread, pyqtSignal
import time

from mss import mss
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import pyperclip
import pytesseract
import os
import json
import re

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
