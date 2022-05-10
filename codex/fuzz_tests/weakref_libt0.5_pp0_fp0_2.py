import weakref
import time
import copy

from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *

from roam.api import GPS, RoamEvents, utils
from roam.gps import GPSBase, GPSException
from roam.utils import log

from roam.structs import CaseInsensitiveDict

from roam.maptools.touchtool import TouchMapTool

from roam.maptools.select import SelectMapTool
from roam.maptools.move import MoveMapTool
from roam.maptools.vertex import VertexMapTool
from roam.maptools.touch import TouchMapTool
from roam.maptools.info import InfoMapTool
from roam.maptools.measure import MeasureMapTool
from roam.maptools.identify import IdentifyMapTool
from roam.maptools.pin import PinMapTool
from roam.maptools.rectangle import RectangleMapTool
from roam.maptools.featuretool import FeatureTool
from roam.maptools.rubberband import RubberBand


class
