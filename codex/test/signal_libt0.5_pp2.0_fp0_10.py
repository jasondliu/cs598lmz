import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import logging
import argparse
import traceback
from functools import partial
from collections import OrderedDict
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QTimer, QEvent, pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.Qt import QUrl
from . import __version__
from .widgets.mainwindow import Ui_MainWindow
from .widgets.mainwidget import MainWidget
from .widgets.aboutdialog import Ui_AboutDialog
from .widgets.preferencesdialog import Ui_PreferencesDialog
from .widgets.logdialog import Ui_LogDialog
from .widgets.helpdialog import Ui_HelpDialog
from .widgets.configdialog import Ui_ConfigDialog
