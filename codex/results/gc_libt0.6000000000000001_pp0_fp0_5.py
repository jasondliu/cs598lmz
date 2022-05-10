import gc, weakref
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtCore import pyqtSlot as Slot
from PyQt5.QtCore import pyqtProperty as Property
from . import splitter, utils

class ChannelGraph(QGraphicsView):
    """
    QGraphicsView for displaying a graph of channel activity.
    """
    def __init__(self, *args, **kwargs):
        super(ChannelGraph, self).__init__(*args, **kwargs)
        self.setViewportUpdateMode(QGraphicsView.SmartViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setStyleSheet("background-color: #222")
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

