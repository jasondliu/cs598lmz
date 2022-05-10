import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore

from .gui import Ui_MainWindow
from . import config
from . import util
from . import dialogs
from . import thread
from . import logger
from . import models
from . import plugin


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('%s %s' % (config.NAME, config.VERSION))

        self.logger = logger.Logger(self.ui.log_text)
        self.logger.info('%s %s' % (config.NAME, config.VERSION))

        self.thread = thread.Thread(self.logger)
        self.thread.finished.connect(self.on_finished)

