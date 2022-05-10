import weakref
from functools import partial
from datetime import datetime
from collections import OrderedDict
from threading import Thread
from queue import Queue

from PyQt5.QtCore import Qt, QObject, QTimer, pyqtSignal, pyqtSlot, QEvent, QSize, QPoint
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QPalette, QBrush, QPainter
