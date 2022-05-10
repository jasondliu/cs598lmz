import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import os
import subprocess
import qdarkstyle

from mainwindow import Ui_MainWindow
from dialog import Ui_Dialog

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openFile)
        self.pushButton_2.clicked.connect(self.dialog)
        self.pushButton_3.clicked.connect(self.run)
        self.pushButton_4.clicked.connect(self.openHelp)
        self.pushButton_5.clicked.connect(self.openAbout)

    def openFile(self):
        self.fileName = QFileDialog.getOpen
