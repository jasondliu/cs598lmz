import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets

import sys
import os

from Ui_MainWindow import Ui_MainWindow
from Ui_AboutDialog import Ui_AboutDialog
from Ui_PreferencesDialog import Ui_PreferencesDialog
from Ui_SelectLanguageDialog import Ui_SelectLanguageDialog

from PyQt5 import QtCore
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QMainWindow, QMessageBox, QShortcut

from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon

from PyQt5.QtGui import QPixmap

from PyQt5.QtCore import QSize

from PyQt5.QtCore import Qt
from PyQt5.QtWid
