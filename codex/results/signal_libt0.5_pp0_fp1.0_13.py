import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon

from . import resources
from .mainwindow import MainWindow
from .dialogs.settings import SettingsDialog
from .dialogs.qrcodedialog import QRCodeDialog
from . import util
from . import bitcoin
from . import network

class MyApp(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)
        self.setWindowIcon(QIcon(":icons/electrum.png"))
        self.setQuitOnLastWindowClosed(False)

        # setup settings
        self.setOrganizationName("Electrum")
        self.setOrganizationDomain("electrum.org")
        self.setApplicationName("Electrum")
        self.setApplicationVersion(electrum.ELECTRUM_VERSION)

        self.load_settings()


