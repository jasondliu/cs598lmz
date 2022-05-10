import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QIcon, QFont, QColor

from ui_mainwindow import Ui_MainWindow

