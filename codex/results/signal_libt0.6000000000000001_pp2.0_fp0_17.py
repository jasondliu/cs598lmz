import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QStyleFactory
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import serial, time, threading, queue, traceback
from serial.tools import list_ports

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(847, 621)
        MainWindow.setMinimumSize(QtCore.QSize(847, 621))
        MainWindow.setMaximumSize(QtCore.QSize(847, 621))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setTabShape(
