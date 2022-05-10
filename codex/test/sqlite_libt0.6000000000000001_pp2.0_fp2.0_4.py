import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import re
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from screen_shot_widget import ScreenShotWidget

class VideoWidget(QWidget):
    def __init__(self, parent=None):
        super(VideoWidget, self).__init__(parent)
        self.setAttribute(Qt.WA_OpaquePaintEvent)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_NativeWindow)
        self.setUpdatesEnabled(False)
        self.video_frame = QImage()

        self.fps = 0.0
        self.bitrate = 0.0
        self.time_elapsed = 0.0
        self.time_remaining = 0.0
        self.size = 0.0

        self.video_is_playing = False
        self.video_is_paused = False
        self.video_is_stopped
