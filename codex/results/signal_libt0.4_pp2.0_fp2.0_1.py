import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, QTimer, pyqtSignal

from ui.mainwindow import MainWindow
from ui.settingswindow import SettingsWindow
from ui.aboutwindow import AboutWindow
from ui.progresswindow import ProgressWindow
from ui.logwindow import LogWindow

from core.settings import Settings
from core.worker import Worker

from core.log import Log

from core.utils import get_version

import os
import sys

class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        self.setApplicationName("Qt-Image-Converter")
        self.setApplicationDisplayName("Qt-Image-Converter")
        self.setApplicationVersion(get_version())

        self.settings = Settings()
        self.settings.load()

        self.log = Log()

        self.worker =
