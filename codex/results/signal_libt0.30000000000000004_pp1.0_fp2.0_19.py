import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .gui import Ui_MainWindow
from . import __version__

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_Quit.triggered.connect(self.close)
        self.ui.action_About.triggered.connect(self.about)
        self.ui.action_About_Qt.triggered.connect(QApplication.instance().aboutQt)
        self.ui.action_About_Qt.triggered.connect(QApplication.instance().aboutQt)
        self.ui.action_About_Qt.triggered.
