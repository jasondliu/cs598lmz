import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_mainwindow import Ui_MainWindow
from ui_dialog import Ui_Dialog
from ui_about import Ui_About
from ui_preferences import Ui_Preferences

from about import About
from preferences import Preferences

from serial import Serial
from serial.tools import list_ports

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.serial = None

        self.actionAbout.triggered.connect(self.showAbout)
        self.actionPreferences.triggered.connect(self.showPreferences)
        self.actionExit.triggered.connect(self.close)

