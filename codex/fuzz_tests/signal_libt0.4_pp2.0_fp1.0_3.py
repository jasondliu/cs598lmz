import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QThread, QTimer, QSize, QPoint, QEvent, Qt, QPointF
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QLabel, QLineEdit, QFileDialog, QInputDialog, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsTextItem, QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem, QGraphicsPathItem, QGraphicsSimpleTextItem, QGraphicsItemGroup, QGraphicsAnchorLayout
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush, QPolygonF, QPainterPath
