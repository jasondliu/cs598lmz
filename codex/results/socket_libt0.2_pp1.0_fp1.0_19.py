import socket
import sys
import time
import threading

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("聊天室")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowFlags(Qt.WindowSystemMenuHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.pushButton.clicked.connect(self.send_msg)
        self.push
