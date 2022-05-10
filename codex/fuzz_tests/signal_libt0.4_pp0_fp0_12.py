import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon

import socket
import sys
import os
import json

class Server(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.host = '127.0.0.1'
        self.port = 8080
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(1)

    def run(self):
        while True:
            conn, addr = self.s.accept()

