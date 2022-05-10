import _struct

from qgis.PyQt.QtWidgets import QApplication, QMessageBox
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtCore import QVariant
from qgis.core import (Qgis,
                       QgsApplication,
                       QgsGeometry,
                       QgsPointXY,
                       QgsWkbTypes,
                       QgsFeature,
                       QgsField,
                       QgsProject,
                       QgsCoordinateReferenceSystem,
                       QgsCoordinateTransform,
                       QgsProcessingFeedback,
                       QgsProcessingUtils,
                       QgsSpatialIndex,
                       QgsVectorLayer,
                       QgsRasterLayer)
from qgis.gui import QgsVertexMarker

from .utilities.tools import tr, logMessage
from .utilities.settings import read_setting, write_setting, set_setting
from .utilities.plugin import get_plugin_path
from .utilities.layer_selector import LayerSelector, LayerSelectorDialog

from
