import gc, weakref
from weakref import WeakValueDictionary
from pprint import pprint

# import sys
# import threading
# import traceback
# import time

import logging
log = logging.getLogger(__name__)
# log.setLevel(logging.DEBUG)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QRect, QPoint, QPointF, QLineF, QObject, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QColor, QPen, QBrush, QImage, QImageReader, QPalette, QPixmap, QFont, QFontMetrics, QIcon
from PyQt5.QtWidgets import QLabel, QWidget, QTabWidget, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy, QScrollArea, QSplitter, QFrame, QCheckBox, QGroupBox, QRadioButton, QButtonGroup, QComboBox, QSpin
