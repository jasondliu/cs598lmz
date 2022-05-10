import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QLabel, QPushButton, QWidget, QGridLayout, QTableView, QAbstractItemView, QHeaderView, QApplication
from PyQt5.QtCore import Qt, QVariant, QModelIndex, QAbstractTableModel, QSize, QPoint, QObject, pyqtSignal, QMimeData, QDataStream, QByteArray
from PyQt5.QtGui import QIcon, QPixmap, QDrag, QDragEnterEvent, QDropEvent, QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.uic import loadUiType
from PyQt5.QtCore import QCoreApplication, QTranslator
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
