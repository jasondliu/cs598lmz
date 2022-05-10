import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from pydynamind import *
from osgeo import ogr

class CreateParcels(Module):
        display_name = "Create Parcels"
        group_name = "Urban Form"

        def __init__(self):
            Module.__init__(self)
            self.setIsGDALModule(True)

            self.createParameter("view_name", STRING)
            self.view_name = "parcel"

            self.createParameter("parcel_area", DOUBLE)
            self.parcel_area = 500

            self.createParameter("parcel_length", DOUBLE)
            self.parcel_length = 50

            self.createParameter("parcel_width", DOUBLE)
            self.parcel_width = 50

            self.createParameter("parcel_height", DOUBLE)
            self.parcel_
