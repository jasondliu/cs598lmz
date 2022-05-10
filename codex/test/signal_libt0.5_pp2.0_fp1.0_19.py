import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit, QCheckBox
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QSizePolicy, QComboBox
from PyQt5.QtWidgets import QProgressBar, QProgressDialog, QDialog

from PyQt5.QtGui import QIcon, QPixmap, QImage, QPainter, QPen, QColor
from PyQt5.QtGui import QTransform, QFont
from PyQt5.QtGui import QFontMetrics

from PyQt5.QtCore import QSize, QPoint, QPointF, QRect, QRectF
