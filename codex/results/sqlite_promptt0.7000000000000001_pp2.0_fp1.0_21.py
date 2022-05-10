import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/serg/Documents/python_projects/db/my_db.db')
from datetime import datetime

from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox)


# PyQt5/Qt Widgets/QLabel
# PyQt5/Qt Widgets/QPushButton
# PyQt5/Qt Widgets/QTextEdit


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Авторизация")
        self.resize(300, 100)
        self.grid = QGridLayout(self)
        self.grid.setSpacing(10)
        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(2, 1)
        self.grid.setRowStretch(
