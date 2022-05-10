import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Initialize Qt resources from file resources.py
import resources


# Import the code for the dialog
from pynode_dialog import pynodeDialog
import os.path
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from PyQt4 import QtCore, QtGui
import os.path, math, random, sys
from qgis.gui import QgsMessageBar
from qgis.core import QgsMessageLog
from qgis.utils import iface


class pynode:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to
