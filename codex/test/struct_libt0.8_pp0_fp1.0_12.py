import _struct
import sys
import threading
import time
import typing
import traceback

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtGui import QColor, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QLabel, QTableWidget, QTableWidgetItem, \
    QHeaderView, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QMessageBox

import msg
import net
import util
import resource


class TableWidget(QTableWidget):
    def __init__(self, *args):
        super(TableWidget, self).__init__(*args)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)


