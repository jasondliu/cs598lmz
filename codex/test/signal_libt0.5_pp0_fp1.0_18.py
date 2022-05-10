import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QTimer

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_preferences import Ui_Preferences

from settings import Settings
from about import About
from preferences import Preferences
from device import Device

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = Settings()
        self.settings.load()

        self.preferences = Preferences(self.settings)
        self.about = About(self.settings)

        self.device = Device(self.settings)

        self.device.set_mode(self.settings.mode)

