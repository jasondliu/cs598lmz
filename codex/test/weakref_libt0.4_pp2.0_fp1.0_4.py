import weakref

from PyQt5.QtCore import Qt, QTimer, QPoint, QPointF
from PyQt5.QtGui import QColor, QPen, QPainterPath, QPainter, QBrush, QFont, QPixmap
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsObject, QGraphicsScene, QGraphicsView, QGraphicsSceneMouseEvent, QApplication, QWidget, QGraphicsSceneContextMenuEvent, QMenu, QAction
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgRenderer

from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget
from python_qt_binding.QtGui import QColor, QPen, QPainterPath, QPainter, QBrush, QFont, QPixmap
from python_qt_binding.QtCore import Qt, QTimer, QPoint, QPointF

from sensor_msgs.msg import JointState
