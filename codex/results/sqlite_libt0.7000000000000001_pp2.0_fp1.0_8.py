import ctypes
import ctypes.util
import threading
import sqlite3
import os
import datetime
import re
import unicodedata

#class for the main window
class main_window(QMainWindow):
    def __init__(self, parent=None):
        super(main_window, self).__init__(parent)
        self.main_ui()
        
    def main_ui(self):
        self.setWindowTitle("Calendar")
        self.setWindowIcon(QIcon("calendar.png"))
        self.setGeometry(100, 100, 1080, 650)
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.bottom_widget = QWidget()
        self.bottom_layout = QHBoxLayout()
        self.bottom_widget.setLayout(self.bottom_layout)
        self.main_layout.addWidget(self.bottom_widget)
        self.add_button = QPushButton(QIcon("add.png
