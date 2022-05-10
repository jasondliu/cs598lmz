import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

import os
import sys
import subprocess
import time
import json

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('自动化测试工具')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(400, 300)

        self.label_apk = QLabel('apk文件路径:')
        self.label_apk.setAlignment(Qt.AlignCenter)
        self.label_apk
