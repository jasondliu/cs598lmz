import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

import os, sys

from otf_raster_section_dialog import OTFRasterSectionDialog

import numpy as np

class OTFRasterSectionTool(QgsMapTool):

	def __init__(self, iface):
		QgsMapTool.__init__(self, iface.mapCanvas())
		self.setCursor(Qt.CrossCursor)
		self.iface = iface

	def canvasPressEvent(self, event):
		pass

	def canvasMoveEvent(self, event):
		pass

	def canvasReleaseEvent(self, event):
		#Get the click
		x = event.pos().x()
		y = event.pos().y()

		#Get the raster under the click
		
