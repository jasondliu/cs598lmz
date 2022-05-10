import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtGui, QtCore, QtWidgets

from .camerasettings import CameraSettings
from .imagesettings import ImageSettings
from .zoomcontrol import ZoomControl
from .gps import Gps
from .tours import Tours
from .overlay import Overlay
from .imageview import ImageView

import time

class Gui(object):
    def __init__(self, app):
        self.app = app
        self.app.setApplicationName("timelapse")

        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("TimeLapse")
        self.window.setWindowIcon(QtGui.QIcon("icon.png"))

        self.timer = QtCore.QTimer(self.window)
        self.timer.timeout.connect(self.onTimer)

        self.thread = QtCore.QThread(self.window)
        self.thread.start()

        self.window.setCentral
