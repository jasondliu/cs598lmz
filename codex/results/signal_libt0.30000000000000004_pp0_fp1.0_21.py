import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui

from . import __version__
from . import __description__
from . import __url__
from . import __author__
from . import __email__
from . import __license__

from . import resources
from . import config
from . import utils
from . import widgets
from . import dialogs
from . import mainwindow
from . import settings
from . import updater

from . import __appname__

import logging
logger = logging.getLogger(__name__)

def main():
    """
    Run the main application.
    """
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Set up application
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName(__appname__)
    app.setOrganizationDomain(__url__)
    app.setApplicationName(__appname__)
    app.setApplicationVersion(__version
