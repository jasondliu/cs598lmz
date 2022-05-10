import socket
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5.QtGui import QTextCursor



class MyThread(QThread):
    mysignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', 9090))
        self.sock.send('Client'.encode('utf-8'))
        self.sock.setblocking(False)

    def run(self):
        while True:
            try:
                data = self.sock.recv(1024)
                self.
