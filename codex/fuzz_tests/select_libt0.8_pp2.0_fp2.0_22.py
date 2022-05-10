import select
import serial
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QGroupBox, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QTextCursor, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
from time import sleep
import cv2
import numpy as np

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.config = json.load(open("config/config.json", "r"))
        self.ser = None
        self.port = self.config["port"]
        self.baudrate = int(self.config["baudrate"])
        self.Delay_time = self.config
