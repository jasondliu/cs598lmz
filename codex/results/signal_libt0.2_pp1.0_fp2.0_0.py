import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from qgis_plugin_dialog import qgis_pluginDialog
import os.path


class qgis_plugin:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'qgis_plugin_{}.qm'.format(locale))

        if
