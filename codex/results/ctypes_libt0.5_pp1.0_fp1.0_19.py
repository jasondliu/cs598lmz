import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from datetime import date

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from app import Ui_MainWindow
from model import Model
from settings import Settings
from about import About
from add_item import AddItem
from add_category import AddCategory
from add_shop import AddShop
from add_currency import AddCurrency
from add_wallet import AddWallet
from add_transaction import Add
