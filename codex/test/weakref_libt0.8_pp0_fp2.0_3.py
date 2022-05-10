import weakref
import rospy
import rospkg

from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget, QAction
from python_qt_binding.QtCore import Qt, QEvent, QObject
from python_qt_binding.QtGui import QPainter, QColor, QPen, QFont, QKeyEvent
from qt_gui.plugin import Plugin

from std_msgs.msg import String
from sensor_msgs.msg import Image

import os
import subprocess

class CustomLabel(QWidget):
    def __init__(self, parent=None):
        super(CustomLabel, self).__init__(parent)
        self.qr = None
        self.image = None
        self.setMinimumHeight(100)
        self.setMinimumWidth(100)

    def set_qr(self, qr):
        self.qr = qr

    def set_image(self, img):
        self.image = img
