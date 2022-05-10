import weakref

from PyQt5.QtCore import pyqtSignal, QObject

from qgis.core import QgsMapLayer, QgsProject, QgsRasterBandStats, QgsRasterTransparency, QgsRasterLayer, QgsSingleBandGrayRenderer
from qgis.gui import QgsMapTool

from .exceptions import MapActionException


LOGGER = logging.getLogger(__name__)


class InvalidRasterLayerSelectedException(MapActionException):
    """Exception thrown when an invalid raster layer is selected in the layer combo box"""

    def __init__(self, layer: QgsMapLayer):
        """Constructor.

        :param layer: The invalid layer selected.
        """
        super().__init__('Invalid raster layer selected: {}'.format(layer), missing_layer=layer)


class NoRasterLayerSelectedException(MapActionException):
    """Exception thrown when no raster layer is selected in the layer combo box"""
