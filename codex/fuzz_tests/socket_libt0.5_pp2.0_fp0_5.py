import socket
import time
import sys
import threading

import cv2
import numpy as np

from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.uic import loadUi


class CamThread(QThread):
    changePixmap = pyqtSignal(np.ndarray)
    changePixmap2 = pyqtSignal(np.ndarray)

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                self.changePixmap.emit(frame)


class CamThread2(QThread):
    changePixmap = pyqtSignal(np.ndarray)
    changePixmap2 = pyqtSignal(np.ndarray)

    def run(self):
        cap = cv2.VideoCapture(1)
        while True
