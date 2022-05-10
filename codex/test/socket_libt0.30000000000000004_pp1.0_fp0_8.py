import socket
import sys
import time

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow

HOST = '127.0.0.1'
PORT = 50007

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.ui.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
        self.ui.pushButton_4.clicked.connect(self.on_pushButton_4_clicked)
