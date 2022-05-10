import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

from PIL import Image

import face_recognition

import argparse
import glob
import sys
import os
import shutil

from search_face.search_face_by_recognition import SearchFaceByRecognition

class FaceRecognitionWidget(QWidget):
    def __init__(self, parent=None):
        super(FaceRecognitionWidget, self).__init__(parent)

        self.parent = parent

        self.setWindowTitle('Face Recognition')
        self.setWindowFlags(Qt.Window)
        self.resize(1000,800)

        self.layout = QGridLayout()

