import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import traceback
import webbrowser

from PyQt5.QtCore import QCoreApplication, QObject, QTimer, pyqtSignal, QEvent
from PyQt5.QtGui import QIcon, QPixmap, QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QAction, QShortcut, QSystemTrayIcon

from . import resources
from .preferences import PreferencesDialog
from .player import Player
from .about import AboutDialog
from .ui import Ui_MainWindow
from .ui_welcome import Ui_WelcomeDialog
from .ui_exit import Ui_ExitDialog
from .ui_download import Ui_DownloadDialog
from .ui_update_available import Ui_UpdateAvailableDialog
from .ui_updater import Ui_UpdaterDialog
from .download_thread import DownloadThread
from .updater import Updater
from .utils
