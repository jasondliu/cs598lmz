import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import os

from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *


from lib import project
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from lib.system import procMath as pMath
from lib.system import procSystem as pSys


class BlurTool(QMainWindow):
    def __init__(self, parent=None):
        """
            @param parent (QtGui.QWidget): Parent widget where to apply blur.
        """
        #-- Get Houdini Main Window --#
        self.parent = parent or pQt.getMayaWindow()
        #-- Get Project Root --#
        self.project = project.Project()
        self.projectRoot = self.project.getRoot()
        #-- Get Houdini Environment --#
        self.houd
