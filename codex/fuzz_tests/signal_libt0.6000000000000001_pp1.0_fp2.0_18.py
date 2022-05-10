import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import time

from PyQt5 import QtCore
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QMessageBox, QAction, QMenu, QSystemTrayIcon, QDialog, \
    QFileDialog, QListWidgetItem, QAbstractItemView, QHeaderView

from ui.Ui_MainWindow import Ui_MainWindow
from ui.Ui_login import Ui_Dialog
from ui.Ui_about import Ui_Dialog as Ui_about
from ui.Ui_config import Ui_Dialog as Ui_config
from ui.Ui_new import Ui_Dialog as Ui_new
from ui.Ui_edit import Ui_Dialog as Ui_edit
from ui.Ui_import import Ui_Dialog as Ui_import
from ui.U
