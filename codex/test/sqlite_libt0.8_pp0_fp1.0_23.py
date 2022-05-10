import ctypes
import ctypes.util
import threading
import sqlite3

from xml.dom.minidom import parseString

from Queue import Queue
from PyQt4 import QtGui, QtCore

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QImage

from ui_ui import Ui_MainWindow

class Worker(QThread):
    changePixmap = pyqtSignal(QImage)
    changeValue = pyqtSignal(int)
    changeValueS = pyqtSignal(int)
    changeLabel = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.exiting = False
        self.__flag = threading.Event()
        self.__flag
