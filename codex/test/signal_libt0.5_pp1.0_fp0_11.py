import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt, QEvent, QTimer, QObject
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtCore import pyqtProperty as Property
from PyQt4.QtCore import pyqtSlot as Slot

from qgis.core import QgsApplication

from roam.api import RoamEvents, RoamInterface, utils
from roam.api.utils import error
from roam.api.plugins import Page


class RoamApp(QObject, RoamInterface):
    """
    Main application class for Roam.

    This class is responsible for starting the application and loading all the
    plugins.
    """
    projectloaded = Signal(object)
    projectclosed = Signal(object)
    projectopening = Signal(object)
    projectopeningerror = Signal(object)
    projectloadederror = Signal(object)
