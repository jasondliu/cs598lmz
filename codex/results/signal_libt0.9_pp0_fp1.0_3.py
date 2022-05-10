import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PySide import QtGui, QtCore
import FreeCADGui as Gui
from FreeCAD import Console, Rotation

from pcbnew.units import *

from partseditor import PartsItem
from FreeCADIO import OutThing
from _Globals import *

from PySide.QtGui import QAxObject
from PySide.QtCore import QTimer

from FreeCADGui import getMainWindow


class ExportPCB(object):
    def __init__(self, filename, PCBPath,
            PCBData,
            padmap, htabpadmap,
            partsmap, htabpartsmap,
            shapes,
            parts, holes
            ):

        self.PCBData=PCBData
        self.parts=parts
        self.filename=filename
        self.PCBPath=PCBPath
        self.padmap=padmap
        self.htabpadmap=padmap
        self.shapes=shapes
        self.l
