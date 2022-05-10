import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QColor, QPalette, QFont

import sys

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('MainWindow')
        self.setWindowIcon(QIcon('../../../icons/icon.png'))

        self.button1 = QPushButton('Button 1')
        self.button2 = QPushButton('Button 2')
        self.button3 = QPushButton('Button 3')

        self.label = QLabel('Label')
        self.label.set
