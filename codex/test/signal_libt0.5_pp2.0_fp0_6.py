import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np

from PyQt5.QtCore import Qt, QPointF, QPoint, QSize, QRectF, QRect, QTimer, QEvent, QLineF, QEventLoop
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QPolygonF, QFont, QTransform, QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsTextItem, QGraphicsRectItem, QGraphicsEllipseItem, QMenu, QGraphicsSceneMouseEvent, QGraphicsSceneContextMenuEvent, QGraphicsLineItem, QApplication, QGraphicsPolygonItem, QGraphicsPixmapItem

from PyQt5.QtCore import QT_VERSION_STR as QT_VERSION
from PyQt5.QtCore import PYQT_VERSION_STR as PYQT_VERSION

from . import utils
from . import settings
