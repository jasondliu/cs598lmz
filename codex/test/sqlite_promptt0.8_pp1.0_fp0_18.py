import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("dictionary.db")

from PyQt5.QtCore import (QAbstractItemModel, QModelIndex, QMimeData, Qt, QVariant)
from PyQt5.QtGui import QColor

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QVBoxLayout, QMenuBar, QMenu, QAction, QMessageBox



class TreeItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []
        self.sison = False

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return len(self.itemData)

