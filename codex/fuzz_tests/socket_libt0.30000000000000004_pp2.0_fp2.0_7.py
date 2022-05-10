import socket
import threading
import time
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from client_gui import Ui_MainWindow


class Client(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Client, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('客户端')
        self.setFixedSize(self.width(), self.height())
        self.pushButton.clicked.connect(self.connect_server)
        self.pushButton_2.clicked.connect(self.send_message)
        self.pushButton_3.clicked.connect(self.disconnect_server)
        self.pushButton_4.clicked.connect(self.send_file)
        self.pushButton_5.clicked.connect(self.recv_file)
        self.pushButton_6.cl
