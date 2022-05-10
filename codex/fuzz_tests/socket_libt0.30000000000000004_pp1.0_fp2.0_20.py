import socket
import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox

from client_ui import Ui_Form


class Client(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send)
        self.pushButton_2.clicked.connect(self.connect)
        self.pushButton_3.clicked.connect(self.disconnect)
        self.pushButton_4.clicked.connect(self.clear)
        self.pushButton_5.clicked.connect(self.exit)
        self.pushButton_6.clicked.connect(self.send_file)
        self.pushButton_7.clicked.connect(self.choose_file)
        self.pushButton_8.clicked.connect(self.save_file
