import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import Qt, QStringListModel, QAbstractListModel, QModelIndex
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickView
from PyQt5.Qt import QUrl

# from PyQt5.QtCore import QCoreApplication
from .mainwindow import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.c = ctypes.CDLL(ctypes.util.find_library('c'))
        self.c.srand(self.c.time(0))
        self.threads
