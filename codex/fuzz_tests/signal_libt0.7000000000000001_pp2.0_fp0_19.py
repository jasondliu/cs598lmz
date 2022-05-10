import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

from Controller import Controller
from View.MainWindow import MainWindow
from View.AboutDialog import AboutDialog
from View.LoadingDialog import LoadingDialog
from View.SettingsDialog import SettingsDialog
from View.MessageBox import MessageBox
from Model.Settings import Settings


class GUI():

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setApplicationName('timex')
        self.app.setApplicationVersion('0.1.0')
        self.app.setQuitOnLastWindowClosed(False)

        self.mainWindow = MainWindow(self)
        self.aboutDialog = AboutDialog(self)
        self.loadingDialog = LoadingDialog(self)
        self.settingsDialog = SettingsDialog(self)
        self.messageBox = MessageBox(self)
