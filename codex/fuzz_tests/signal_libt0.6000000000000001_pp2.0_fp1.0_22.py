import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import Qt, QRect, QThread
from PyQt5.QtCore import QPoint

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

from src.User import User
from src.Tasks import Tasks
from src.Task import Task
from src.Queue import Queue
from src.Chart import Chart
from src.Scheduler import Scheduler

from src.ui.MainWindow import Ui_MainWindow
from src.ui.DialogAdd import Ui_
