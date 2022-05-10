import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel, QMenu, QAction
from PyQt5.QtCore import QTimer, QObject, pyqtSignal
from PyQt5.QtCore import QSize, Qt, QPoint

import sys
import os.path

from qt_image_viewer import *
from image_utils import *

class ImageViewer(QtWidgets.QMainWindow):

    def __init__(self):
        super(ImageViewer, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image Viewer")

        self.image_display = QtWidgets.QLabel(self)
