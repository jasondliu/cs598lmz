import ctypes
import ctypes.util
import threading
import sqlite3
from datetime import datetime, timedelta
import time
from sqlite_utils import Database
from sqlite_utils.db import NotFoundError, ForeignKeyConstraintError

from pymultiwii import MultiWii

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot, QThread, pyqtSignal, QTimer
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QApplication, QMessageBox

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

from gui import Ui_MainWindow

import matplotlib.pyplot as plt

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
pg.setConfigOption('antialias', True)


class GetDataThread(QThread):
    """ Thread to get data from the drone """
    newData = py
