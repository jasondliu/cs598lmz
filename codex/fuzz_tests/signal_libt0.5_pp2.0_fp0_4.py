import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_about import Ui_About

class About(QtGui.QDialog):
    """
    About dialog
    """
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_About()
        self.ui.setupUi(self)
        self.setWindowTitle('About')
        self.ui.btnOK.clicked.connect(self.accept)
        self.ui.lblVersion.setText('Version %s' % parent.version)
        self.ui.lblVersion.setText('Version %s' % parent.version)
        self.ui.lblIcon.setPixmap(QtGui.QPixmap(':/images/icon.png'))
        self
