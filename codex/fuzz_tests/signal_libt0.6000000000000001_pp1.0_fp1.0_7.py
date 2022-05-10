import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import math
import time
import json
import re

try:
    from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWidgets import QMainWindow, QWidget
    from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
    from PyQt5.QtWidgets import QLabel, QLineEdit, QTableWidget, QTableWidgetItem
    from PyQt5.QtWidgets import QPushButton, QMessageBox, QFileDialog
    from PyQt5.QtWidgets import QProgressBar, QSlider, QAction
    from PyQt5.QtGui import QIcon, QFont
    from PyQt5.QtMultimedia import QMediaContent, Q
