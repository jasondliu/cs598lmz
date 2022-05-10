import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

class IconWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("PyQt5 Icon")
        self.setWindowIcon(QIcon("icon.png"))
        screen = QApplication.desktop().screenGeometry()
        self.resize(screen.width(), screen.height())
        QMainWindow.setCursor(self, QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.icon = QLabel(self)
        self.icon.setP
