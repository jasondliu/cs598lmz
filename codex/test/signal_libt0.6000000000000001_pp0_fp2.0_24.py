import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings, QLocale
from PyQt5.QtCore import QTranslator, QLibraryInfo

from . import __version__
from .mainwindow import MainWindow
from .settings import Settings
from .plugins.pluginmanager import PluginManager
from .utils import find_data_file
import os


class Application(QApplication):
    def __init__(self, args, locale=QLocale.system().name()):
        super(Application, self).__init__(args)
        self.setOrganizationName("pavlov")
        self.setOrganizationDomain("pavlov.pro")
        self.setApplicationName("pavlov")
        self.setApplicationVersion(__version__)
        self.setWindowIcon(QIcon(find_data_file("pavlov.svg")))
        self.setStyle('Fusion')

        self.settings = Settings()

