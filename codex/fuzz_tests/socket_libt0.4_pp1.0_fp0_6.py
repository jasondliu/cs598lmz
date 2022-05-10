import socket
import sys
import threading
import time
from time import sleep
import struct

from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QPushButton, QLineEdit, QMessageBox, QFileDialog, QProgressBar
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
import PyQt5.QtCore
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QPushButton, QLineEdit, QMessageBox, QFileDialog, QProgressBar
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
import PyQt5.QtCore

from client import Client

class MyThread(QThread):
    change_value
