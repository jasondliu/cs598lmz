import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
"""
import sys
sys.path.insert(0, "..")

import logging
import logging.config
logging.config.fileConfig("./logger.conf")
logger = logging.getLogger("aurora")

from filemanager import AurFileManager
from gui_lib.customDialogs import AurFileDialog
from gui_lib.ui import AurPlayer, AurPlayer_Ui_MainWindow

from PySide import QtCore
from PySide.QtGui import *

import icons


class Main(AurPlayer):
	def __init__(self, parent, fmanager):
		AurPlayer.__init__(self, parent)
		self.fmanager = fmanager
		self.setWindowIcon(QIcon(icons.aurora))
		self.setupUi(self)
		self.initMenus()
		self.initSignals()

	def initMenus(self):
		actions = self.actionList()
		self
