import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import cv2
import os

from PyQt5.QtCore import Qt, QTimer, QThread, QSize, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

from face_detector import FaceDetector
from face_recognizer import FaceRecognizer


class FER(QMainWindow):
    def __init__(self):
        super(FER, self).__init__()
        loadUi("GUI//main.ui", self)

        self.image_label.setScaledContents(True)
        self.set_image_label(cv2.imread("space.jpg"))

        self.start_btn.clicked.connect(self.start)
