import socket
import sys
import time
import threading
import queue
import json

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QLabel, QMessageBox, QProgressBar, QTableWidget, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt, QThread, QObject, pyqtSignal

from server_thread import ServerThread
from client_thread import ClientThread

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'P2P File Sharing'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

       
