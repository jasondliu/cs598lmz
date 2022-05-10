import gc, weakref
from time import time as now

try:
    # PySide
    from PySide import QtGui, QtCore, QtGui as QtWidgets
    try:
        _fromUtf8 = QtCore.QString.fromUtf8
    except AttributeError:
        _fromUtf8 = lambda s: s
except ImportError:
    # PyQt4
    from PyQt4 import QtGui, QtCore
    from PyQt4.QtGui import QApplication


class Form(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # list of items
        self.items = [self.Item("Item %d" % i) for i in range(1000)]

        # Monitor memory usage
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._mem_timer)
        self.timer.start(1000)

        # Create a button to delete the items
        self.btn = QtGui
