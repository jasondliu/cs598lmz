import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import qgis.utils

# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from batch_dialog import BatchDialog
import os.path
import os
import sys
import traceback
import shutil
import re
import time
import subprocess
import tempfile
import webbrowser


class Batch:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
