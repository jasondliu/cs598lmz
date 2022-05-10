import types
types.ClassType=type
types.InstanceType=type
from PyQt4 import QtCore, QtGui
from ui.ui_compare import Ui_Dialog
import sys, os, time, datetime
from qgis.core import *
from qgis.gui import *
from pyspatialite import dbapi2 as sqlite3
from utils import uf, ug

class MyCompDialog(QtGui.QDialog):
    def __init__(self, iface):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #initialize the CANVAS
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.initGui()

    def initGui(self):
        self.ui.toolButton.clicked.connect(self.select_db)
        self.ui.useSelected.clicked.connect(uf.check_use_selected)
        self.ui
