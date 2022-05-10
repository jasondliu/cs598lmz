import socket
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QSizePolicy

from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    """
    GUI for the client application.
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.frame.setVisible(False)
        self.ui.frame_2.setVisible(False)
        # self.ui.label.setVisible(False)
        self.ui.pushButton_2.setVisible(False)

        # self.ui.label.setVisible(False)

