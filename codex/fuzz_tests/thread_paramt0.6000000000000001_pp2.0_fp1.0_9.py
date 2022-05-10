import sys, threading
threading.Thread(target=lambda:sys.stdout.write('')).start()

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except ImportError:
    from PySide.QtGui import *
    from PySide.QtCore import *

from pymel.all import *

from . import utils

class JointsWindowClass(QMainWindow):
    def __init__(self, parent=None):
        super(JointsWindowClass, self).__init__(parent)
        self.ui = utils.loadUi(__file__, self)
        self.setWindowTitle('Joints')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setMinimumSize(self.size())
        self.setMaximumSize(self.size())
        self.ui.createBtn.clicked.connect(self.create_joints)
        self.ui.jointsSpin.valueChanged.connect(self.update_preview)
        self.ui.j
