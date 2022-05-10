import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from . import gui
from . import config
from . import core
from . import utils

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("TinyTinyRSS")
    app.setOrganizationName("TinyTinyRSS")
    app.setOrganizationDomain("tt-rss.org")
    app.setApplicationVersion(core.__version__)

