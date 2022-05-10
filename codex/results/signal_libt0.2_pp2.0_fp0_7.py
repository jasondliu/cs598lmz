import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

from . import __version__
from . import __appname__
from . import __description__
from . import __url__
from . import __author__
from . import __email__
from . import __license__

from . import config
from . import logger
from . import utils
from . import resources
from . import i18n
from . import settings
from . import updater
from . import mainwindow
from . import trayicon
from . import updater
from . import updater_qt

from . import __file__ as __appfile__

class Application(QApplication):
    def __init__(self, argv):
        super(Application, self).__init__(argv)
        self.setApplicationName(__appname__)
        self.setApplicationVersion(__version__)
        self.setOrganizationName(__appname__)
        self
