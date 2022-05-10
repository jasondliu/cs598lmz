import ctypes
import ctypes.util
import threading
import sqlite3
from datetime import datetime
import os
import pickle

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTreeWidgetItem, QWidget
from PyQt5.QtGui import QPixmap, QScreen, QCloseEvent
from PyQt5.QtCore import QPoint, QTimer, QDate

from view import View
from model import Model
import configuration as conf
from connection_dlg import ConnectionDialog


class Controller(QMainWindow):

    def __init__(self):
        super().__init__()
        self.view = View(self)
        self.model = Model()

        self.connection_dlg = ConnectionDialog(self.view)

        self.view.status_bar.showMessage("Не подключено к базе данных.")
