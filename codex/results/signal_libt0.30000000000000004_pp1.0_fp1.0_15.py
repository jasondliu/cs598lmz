import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import threading
import traceback
import subprocess

from PyQt5 import QtCore, QtWidgets, QtGui

from . import config
from . import gui
from . import utils
from . import __version__

from . import _tray
from . import _settings
from . import _about
from . import _logs
from . import _editor
from . import _updater
from . import _notifier
from . import _watcher

from . import _app_updater
from . import _app_notifier
from . import _app_watcher

from . import _app_settings
from . import _app_about
from . import _app_logs
from . import _app_editor

from . import _app_tray

from . import _app_main

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed
