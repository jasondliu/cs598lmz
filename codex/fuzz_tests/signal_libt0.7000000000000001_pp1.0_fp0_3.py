import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt5 import QtCore, QtGui, QtWidgets
from . import _window_ui
from . import _window_ui_basic
from . import _window_ui_precalc

# -----------------------------------------------------------------------------

class Window(QtWidgets.QMainWindow):
    def __init__(self, app, parent=None):
        super(Window, self).__init__(parent)
        self.app = app
        self.ui = _window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionAbout_Qt.triggered.connect(self.app.aboutQt)
        self.ui.actionAbout_this_program.triggered.connect(self.about)

        self.ui.actionBasic.triggered.connect(self.openBasic)
        self.ui.actionPrecalc.triggered
