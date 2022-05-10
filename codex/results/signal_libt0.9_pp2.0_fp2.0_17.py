import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore

from qgis.core import *
from qgis.gui import *

from qrcode_layer import QrcodeLayer, QRcodeFeatures
from add_new_geocode import AddNewGeocode
from dialogs import PhotoRotationDialog
from FileSizeDialog import FileSizeDialog
from QrCodeListDialog import QrCodeListDialog
from DbFileSizeDialog import DbFileSizeDialog
import dropbox
import csv
from cStringIO import StringIO

# Initialize Qt resources from file resources.py
import resources_rc

# Import the code for the dialog
from geocode_dialog import GeocodeDialog
import os.path


class Geocode:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        #
