import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsLineItem, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPen, QColor, QBrush, QPolygonF, QPainter, QPainterPath, QPalette, QTransform
from PyQt5.QtCore import Qt, QPointF


class QGraphicsPolygonItem(QGraphicsItem):
    def __init__(self, parent=None):
        super(QGraphicsPolygonItem, self).__init__(parent)
        self.polygon = QPolygonF()
        self.fillColor = QColor(0, 0, 0, 0)

    def paint(self, painter, option, widget):
        painter.setBrush(self.fillColor)
        painter.drawPolygon(self.polygon)

    def boundingRect(self):
        return self.polygon.boundingRect()


class QGraphicsPolygonItem2(QGraphicsItem):
