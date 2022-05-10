import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from copy import copy
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QFileDialog

from PyQt5.QtGui import QImage, QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt, QTimer

class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QImage()
        self.image_display = QLabel()
        self.image_display.setBackgroundRole(QPalette.Base)
        self.image_display.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image_display.setScaledContents(True)
        self.image_display.setPixmap(QPixmap.fromImage(self.image))

        hbox = QHBoxLayout()
       
