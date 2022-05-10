import ctypes
ctypes.cast(0, ctypes.py_object)

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from qgis.networkanalysis import *

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from qgis_plugin_tools.tools.i18n import tr
from qgis_plugin_tools.tools.settings import plugin_name
from qgis_plugin_tools.tools.resources import *
from qgis_plugin_tools.tools.exceptions import *
from qgis_plugin_tools.tools.version import version
from qgis_plugin_tools.tools.utils import *
from qgis_plugin_tools.gui.dialogs.about_dialog import AboutDialog
from qgis_plugin_tools.gui.dialogs.settings_dialog import SettingsDialog
from qgis_plugin
