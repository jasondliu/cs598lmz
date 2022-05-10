import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QFileDialog, QTableWidgetItem, QTableWidget, QLabel
from PyQt5.QtWidgets import QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QScrollArea, QSpacerItem
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QFileDialog, QTableWidgetItem, QTableWidget, QLabel
from PyQ
