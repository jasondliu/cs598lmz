import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMessageBox
from qgis.core import QgsVectorLayer, QgsProject, QgsFeature, QgsGeometry, QgsPointXY, QgsField, QgsFields, QgsVectorFileWriter, QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsWkbTypes
from qgis.gui import QgsMapToolEmitPoint, QgsRubberBand

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .cadastre_ch_dialog import CadastreChDialog
import os.path


class CadastreCh:
    """QGIS Plugin Implementation."""
