import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, uic
from PyQt4.QtGui import QFileDialog
from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtCore import pyqtSlot

from kite.views import KiteView
from kite.controllers import KiteController

from kite.config import Config
from kite.utils import get_resource_path

from kite.widgets.qtutils import get_ui_file, get_icon_file


class KiteWindow(QtGui.QMainWindow):
    """
    The main window of the Kite application.
    """

    def __init__(self):
        super(KiteWindow, self).__init__()

        self.ui = uic.loadUi(get_ui_file('kite.ui'), self)

        self.view = KiteView(self)
        self.controller
