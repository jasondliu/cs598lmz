import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtXml import *
from PyQt5.Qsci import *

from . import __version__, __author__
from .config import Config, ConfigDialog
from .finddialog import FindDialog
from .gotodialog import GotoDialog
from .textedit import TextEdit
from .mainwindow import MainWindow


class Application(QApplication):
    def __init__(self, args):
        super(Application, self).__init__(args)
        self.setApplicationName("QScintilla Demo")
        self.setOrganizationName("Riverbank Computing")
        self.setOrganizationDomain("riverbankcomputing.com")
        self.setApplicationVersion(__version__)

        self.config = Config()

