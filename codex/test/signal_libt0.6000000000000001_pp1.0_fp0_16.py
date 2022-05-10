import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from ui_loadingdialogbase import Ui_LoadingDialogBase


class LoadingDialog(QDialog, Ui_LoadingDialogBase):
    def __init__(self, iface, parent=None):
        QDialog.__init__(self, parent)
        self.iface = iface
        self.setupUi(self)
        self.updateTimer = QTimer()
        QObject.connect(self.updateTimer, SIGNAL("timeout()"), self.updateProgress)
        self.updateTimer.start(1000)


    def updateProgress(self):
        self.progressBar.setValue(self.progressBar.value() + 1)

    def setProgressRange(self, minimum, maximum):
        self.progressBar.setRange(minimum, maximum)

