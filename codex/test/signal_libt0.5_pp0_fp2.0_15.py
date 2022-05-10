import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# This is necessary so that the QGIS libraries are loaded in the correct order
from qgis.core import QgsApplication
# Make sure QGIS_PREFIX_PATH is set in your env if needed!
qgs = QgsApplication([], False)
qgs.initQgis()

from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

app = QApplication([])
canvas = QgsMapCanvas()
canvas.setCanvasColor(Qt.white)
canvas.enableAntiAliasing(True)
canvas.setWindowTitle("Hello World")

# Add the layer
vl = QgsVectorLayer("/home/koko/Documents/Data/Samples/qgis_sample_data/shapefiles/alaska.shp", "alaska", "ogr")
