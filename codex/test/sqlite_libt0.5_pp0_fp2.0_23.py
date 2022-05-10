import ctypes
import ctypes.util
import threading
import sqlite3

from PyQt5.QtCore import pyqtSlot, QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from . import settings
from . import ui
from . import config
from . import i18n
from . import util
from . import __version__


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.setWindowIcon(QIcon(util.get_resource('icon.png')))
        self.setApplicationVersion(__version__)
        self.setApplicationName('todos')

        settings.init()
        i18n.init()

        self.main_window = ui.MainWindow()
        self.main_window.show()

        self.notify_thread = NotifyThread(self)
        self.notify_thread.start()


