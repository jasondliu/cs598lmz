import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSignal

from . import config
from . import mainwindow
from . import util
from . import log
from . import db
from . import models
from . import controller
from . import updater
from . import plugins
from . import settings
from . import resources
from . import exceptions

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setApplicationName(config.APP_NAME)
        self.setApplicationVersion(config.VERSION)
        self.setOrganizationName(config.ORGANIZATION_NAME)
        self.setOrganizationDomain(config.ORGANIZATION_DOMAIN)

        self.logger = log.get_logger(__name__)

        self.settings = settings.Settings()
        self.settings.load()

        self.db = db.DB
