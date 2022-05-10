import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from . import settings
from . import util
from . import gui
from . import backend


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.setApplicationName("Bubbles")
        self.setApplicationVersion("0.1")
        self.setOrganizationName("bubbles")
        self.setOrganizationDomain("bubbles.com")

        self.settings = settings.Settings()

        self.backend = backend.Backend(self)

        self.windows = []
        self.create_window()

    def create_window(self):
        window = gui.Window(self)
        window.show()
        self.windows.append(window)

    def quit(self):
        for window in self.windows:
            window.
