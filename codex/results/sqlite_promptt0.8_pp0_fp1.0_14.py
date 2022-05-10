import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/tmp/peerdb.db')

import gi
gi.require_version('Gtk', '3.0')
import Gtk

import pypyodbc

# Import PyQt5 elements
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtWidgets import (QApplication, QDialog, QTableView, QVBoxLayout,
                             QGroupBox, QLabel, QLineEdit, QPushButton)
from PyQt5.QtGui import QPalette, QColor, QFont

# Import ldap elements
import ldap
from ldap.controls import SimplePagedResultsControl

PEERS_IN_GROUP = 100
PEERS_PER_PAGE = 100

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self
