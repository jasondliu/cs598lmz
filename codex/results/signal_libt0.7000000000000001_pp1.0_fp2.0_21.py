import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, QMainWindow, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
import sys
from PIL import Image
import argparse

class Button(QPushButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(text, parent)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Py
