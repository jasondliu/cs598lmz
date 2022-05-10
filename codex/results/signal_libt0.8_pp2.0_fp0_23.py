import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QObject, QProcess, QFile, QFileInfo, QIODevice, pyqtSignal
from PyQt5.QtWidgets import QListView, QGridLayout, QLineEdit, QCompleter, QLabel, QPushButton, QCheckBox, QDialog, QProgressBar, QFileDialog
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QKeySequence, QFont, QFontMetrics

from .widgets.ui_window import Ui_MainWindow
from .widgets.ui_connect_dialog import Ui_Dialog
from .widgets.ui_about_dialog import Ui_AboutDialog

from .. import __version__
from ..common.globals import Globals

from ..lib.process import Process
from ..lib.data_model import DataModel
from ..lib.completer_
