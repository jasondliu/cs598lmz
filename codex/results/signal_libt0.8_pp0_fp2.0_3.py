import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt4.uic import loadUiType
from PyQt4.QtGui import QDesktopServices

from qgis.core import QgsApplication

# initialize Qt resources from file resouces.py
import resources_rc
# Import the code for the dialog
from pydevd_client_dialog import pydevdClientDialog
import pydevd_client_utils
import pydevd_client_constants

class pydevdClientPlugin:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_
