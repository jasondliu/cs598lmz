import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from qgis_pds_import_dialog import qgis_pds_importDialog
import os.path

# Import custom modules
import pds_db
import pds_utils
import pds_import_utils
import pds_import_dialog
import pds_import_settings
import pds_import_settings_dialog
import pds_import_settings_dialog_new
import pds_import_settings_dialog_edit
import pds_import_settings_dialog_delete
import pds_import_settings_dialog_copy
import pds_import_settings_dialog_
