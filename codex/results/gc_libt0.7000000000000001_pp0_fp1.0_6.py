import gc, weakref

from PyQt5 import QtCore, QtGui, QtWidgets

#import matplotlib.pyplot as plt
#import matplotlib.widgets
#import matplotlib.transforms as mtransforms
#import matplotlib.artist as artist

from . import standard_widgets as sw
from . import pyqtgraph as pg
import pyqtgraph.widgets.RemoteGraphicsView.RemoteGraphicsView as rgv
from . import draggable_rectangle
import numpy as np

class MyGraphicsView(pg.GraphicsView):
    def __init__(self):
        super(MyGraphicsView, self).__init__()
        self.setMouseTracking(True)
        self.setAcceptDrops(True)

    def mouseMoveEvent(self, ev):
        pass

    def mousePressEvent(self, ev):
        pass

    def mouseDoubleClickEvent(self, ev):
        pass

class ImageViewer(QtWidgets.QWidget):
    def __init__(self, parent, name, title, im_shape
