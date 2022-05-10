import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import pygtk
pygtk.require('2.0')
import gtk

import os
import sys
import subprocess
import time
import shutil

from settings import Settings
from utils import *
from config import Config
from menu import Menu
from window import Window
from dialogs import *
from trayicon import TrayIcon
from autostart import Autostart
from about import About
from preferences import Preferences
from updater import Updater
from installer import Installer
from uninstaller import Uninstaller
from launcher import Launcher
from updater import Updater
from updater import UpdateResult

class Main:
    def __init__(self):
        self.settings = Settings()
        self.config = Config()
        self.menu = Menu(self)
        self.window = Window(self)
        self.trayicon = TrayIcon(self)
        self.autostart = Autostart()
        self.updater = Updater(self)
        self.installer =
