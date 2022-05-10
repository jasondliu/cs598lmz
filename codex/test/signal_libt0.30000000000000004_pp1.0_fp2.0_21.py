import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

import os
import sys
import subprocess
