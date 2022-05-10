import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui.MainWindow import MainWindow
from ui.AboutWindow import AboutWindow
from ui.SettingsWindow import SettingsWindow
from ui.HelpWindow import HelpWindow
from ui.ExportWindow import ExportWindow

from settings import Settings

from data.Database import Database
from data.Data import Data

from ui.utils import set_style

from utils import get_logger

logger = get_logger(__name__)


class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        self.main_window = MainWindow()
        self.about_window = AboutWindow()
        self.settings_window = SettingsWindow()
        self.help_window = HelpWindow()
        self.export_window = ExportWindow()

        self.settings = Settings()
        self.data = Data()
