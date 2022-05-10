import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import logging
logging.basicConfig(level=logging.INFO)

from sys import argv, exit
from getopt import getopt, GetoptError
from PyQt5 import QtWidgets, QtCore

from main_window import MainWindow
from update_checker import UpdateChecker
from settings import Settings
from video import Video
from video_list_model import VideoListModel


class Application(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(argv)

        self.setOrganizationName("Minijim")
        self.setApplicationName("Minijim")
        self.setApplicationVersion("0.2.2")

        self.setQuitOnLastWindowClosed(False)

        self.set_ui()
        if self.first_launch:
            self.show_settings()

        self.update_checker = UpdateChecker(self)

        self.window.show()
        self.window.show_
