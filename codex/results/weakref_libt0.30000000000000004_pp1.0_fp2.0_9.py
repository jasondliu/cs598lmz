import weakref
from functools import partial
from datetime import datetime
from collections import OrderedDict
from threading import Thread
from queue import Queue

from PyQt5.QtCore import Qt, QObject, QTimer, pyqtSignal, pyqtSlot, QEvent, QSize, QPoint
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QPalette, QBrush, QPainter
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox, QSpinBox, QDoubleSpinBox, QSlider, QFrame, QSizePolicy, QMenu, QAction, QApplication, QStyle, QStyleOptionSlider, QStylePainter

from electrum_ltc.i18n import _
from electrum_ltc.util import (format_time, format_satoshis, format_fee_satoshis, format_satoshis_plain,
                           format_fee
