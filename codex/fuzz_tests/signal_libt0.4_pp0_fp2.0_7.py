import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from . import icons
from . import utils
from . import settings
from . import widgets

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Pardus Package Manager")
        self.setWindowIcon(QIcon(":/icons/pisi-package-manager.png"))

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.mainWidget = QStackedWidget(self)
        self.setCentralWidget(self.mainWidget)

        self.setupActions()
        self.setupUi()

    def setupActions(self):
        self.actionExit = QAction(QIcon(":/icons/application-exit
