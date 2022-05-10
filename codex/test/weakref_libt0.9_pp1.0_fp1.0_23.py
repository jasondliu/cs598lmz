import weakref
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QInputDialog, QAction, QWidget, QDockWidget, QApplication, QMenu
from PyQt5.QtGui import QFont, QMouseEvent, QPainter, QPalette, QPen, QWindowStateChangeEvent, QIcon, QBrush
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, Qt, QSize, QPointF
from PyQt5 import uic
from calc_model import Model
from equ.equation import Equation


class WidgetList(QWidget):
    def __init__(self, updater):
        super().__init__()
        self.updater = updater
        self.vars = []
        self.equations = []
        self.signal = [pyqtSignal() for _ in range(3 * len(Model.equations) + len(Model.variables))]
        self.lay = []

