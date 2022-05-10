import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSettings

from ui.mainwindow import Ui_MainWindow
from ui.settingsdialog import Ui_SettingsDialog
from ui.aboutdialog import Ui_AboutDialog
from ui.helpdialog import Ui_HelpDialog

from src.tab import Tab
from src.settings import Settings
from src.about import About
from src.help import Help

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = Settings()
        self.about = About()
        self.help = Help()

        self.tabs = []
        self.currentTab = None

        self.set
