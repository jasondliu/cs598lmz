import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import sys
import os

from PyQt5.QtCore import Qt, QSize, QTimer, QLineF, QPointF
from PyQt5.QtGui import QImage, QPainter, QPen, QPolygonF, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import cv2

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, Q
