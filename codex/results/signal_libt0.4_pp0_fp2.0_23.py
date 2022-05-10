import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QShortcut

from . import __version__
from . import config
from . import controller
from . import database
from . import gui
from . import log
from . import model
from . import settings
from . import utils

logger = log.get_logger(__name__)


class MainWindow(QMainWindow):
    """Main window of the application."""

    def __init__(self, app, args):
        super().__init__()
        self.app = app
        self.args = args
        self.config = config.Config()
        self.settings = settings.Settings()
        self.db = database.Database(self.config)
        self.controller = controller.Controller(self.config, self.db)
        self.gui = gui
