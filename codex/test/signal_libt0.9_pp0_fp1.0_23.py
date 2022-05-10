import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from gi.repository import GLib
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from time import time
from qtermwidget import QTermWidget
from controller import TerminalController
from settings import Settings
from profile import Profile
from updater import UpdateChecker
from pprint import pprint
from ui_qdb import Ui_Qdb
from db import DB
from menu import QdbMenu
import sys
import os
import json
from datetime import date
import sqlite3 as dbapi

class QDBTerminal(QWidget):

    def __init__(self, argv):
        super(QDBTerminal, self).__init__()
        self.argv = argv
        self.con = None
        self.settings = Settings()
        self.curprofile = self.settings.load_profile()
        pprint(self.curprofile)
        self.show()
        self.currentDir = os.getcwd()

