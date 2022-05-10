import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os

from PyQt5 import QtGui, QtCore
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt5.QtWidgets import *

#from qgis.core import QgsVectorFileWriter, QgsCoordinateReferenceSystem, QgsCoordinateTransform
from qgis.core import *
from qgis.utils import *

from .lib import util
from .lib import tools
from .lib import plugin
from .lib import file
from .lib import files
from .lib import logger
from .lib import config
from .lib import user
from .lib import roles
from .lib import mapmod
from .lib import template
from .lib import repository
from .lib import git
from .lib import copyset
from .lib import exportsets
