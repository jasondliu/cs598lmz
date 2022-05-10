import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication
import re
import os
import sys

from .main_window import MainWindow
from . import utils
from . import config


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("jwilm")
    app.setOrganizationDomain("github.com/jwilm/alacritty")
    app.setApplicationName("alacritty-colorscheme")
    app.setApplicationVersion(config.VERSION)

    # load settings
    settings = QSettings()
    alacritty_config_path = settings.value("alacritty_config_path", "", type=str)

    # detect alacritty config path
    if not alacritty_config_path:
        alacritty_config_path = utils.get_alacritty_config_path()
        if al
