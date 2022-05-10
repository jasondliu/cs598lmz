import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from ui.gui import Ui_MainWindow
from ui.settings import Ui_Dialog
from ui.add_camera import Ui_add_camera
from ui.add_server import Ui_add_server
from ui.about import Ui_AboutDialog
from ui.camera_settings import Ui_camera_settings

from client import Client

import sys
import os
import time
import select
import optparse
import struct

class AboutDialog(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_AboutDialog()
		self.ui.setupUi(self)

class addCameraDialog(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self
