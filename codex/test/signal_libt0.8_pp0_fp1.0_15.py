import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

from PySide.QtCore import *
from PySide.QtGui import *

from .internal import option


__all__ = ['QtLoop']


class QtLoop:

    _instance = None
    _app = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._app = QApplication(sys.argv)
            cls._instance = super(QtLoop, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        self._quit_handlers = []

    def quit(self):
        self._app.quit()

    def run(self):
        self._app.exec_()

    def add_quit_handler(self, handler):
        self._quit_handlers.append(handler)

    def remove_quit_handler(self, handler):
        self._quit_handlers.remove(handler)

   
