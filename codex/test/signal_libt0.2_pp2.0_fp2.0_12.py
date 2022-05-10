import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_settings import Ui_Settings

from settings import Settings
from about import About
from main import Main

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Qt-приложение")
        self.setWindowIcon(QIcon('icon.png'))
        self.action_about.triggered.connect(self.about)
        self.action_settings.triggered.connect(self.settings)
        self.action_exit.triggered.connect(self.close)
