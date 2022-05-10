import gc, weakref

from PyQt5.QtCore import QCoreApplication, QObject, QMetaObject, QModelIndex, \
    QRectF, QSize, Qt, QEvent
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPen, QBrush, QColor, QFont, QConicalGradient, QLinearGradient, QRadialGradient
import random

from .analogclock_rc import *
from .scene import QGraphicsSceneDragDropEvent, QGraphicsView


def _unsetCursor(widget):
    widget.setCursor(QCursor())

def _setCursor(widget, shape):
    widget.setCursor(QCursor(shape))
   
