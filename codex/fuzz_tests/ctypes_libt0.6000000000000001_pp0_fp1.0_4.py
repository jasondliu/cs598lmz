import ctypes
ctypes.windll.user32.MessageBoxW(None, "Your text", "Your title", 1)

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip,
                             QMessageBox, QDesktopWidget, QMainWindow, QAction, qApp,
                             QMenu, QLabel, QInputDialog, QLineEdit, QTextEdit, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QGroupBox, QDialog, QFileDialog,
                             QProgressBar)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show
