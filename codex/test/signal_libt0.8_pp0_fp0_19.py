import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QSplitter, QGridLayout, QTableWidget, QTableWidgetItem, QProgressBar, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
import sys, os
import pandas as pd

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.openFileNamesDialog()
 
        self.show()
 

