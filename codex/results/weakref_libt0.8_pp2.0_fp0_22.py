import weakref
import xml.dom.minidom
from xml.dom.minidom import Node
from xml.dom.minidom import parse, parseString

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush, QColor, QPolygonF
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPolygonItem, QGraphicsObject


class GoPolygon(QGraphicsPolygonItem):
    """The GoPolygon class is a re-engineered version of
    QGraphicsPolygonItem providing a layer of indirection between
    QGraphicsPolygonItem and the user of the class.

    The GoPolygon class suppports the following properties
    * shadow,
    * fill and outline colour
    * outline pen width
    * outline pen style
    * outline pen cap style
    * outline pen join style
    * perimeter
    * area
    * position of the center of gravity
    as well as the properties provided by QGraphicsPolygonItem itself.

    """
