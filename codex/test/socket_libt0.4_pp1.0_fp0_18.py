import socket
import sys
import time
import threading

from PyQt5.QtCore import QObject, pyqtSignal, QThread

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

class Server(QObject):
    def __init__(self, parent=None):
        super(Server, self).__init__(parent)
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(('', 1234))
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()
        self.conn.send(bytes('Welcome to the server!', 'utf-8'))
        self.data = self.conn.recv(1024)
