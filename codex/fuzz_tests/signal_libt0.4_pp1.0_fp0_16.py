import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets

from . import config
from . import main_window
from . import preferences_dialog
from . import upgrade_dialog
from . import util
from . import version
from . import web
from . import web_dialog


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.web_view = web.WebView(self)
        self.web_view.setUrl(QtCore.QUrl(config.get('web', 'url')))
        self.web_view.loadFinished.connect(self.web_view_load_finished)
        self.web_view.urlChanged.connect(self.web_view_url_changed)
        self.web_view.titleChanged.
