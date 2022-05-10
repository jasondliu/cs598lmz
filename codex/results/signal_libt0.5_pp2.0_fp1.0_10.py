import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QTabWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QCheckBox, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from main_window import Ui_MainWindow
from about_window import Ui_aboutWindow
from settings_window import Ui_settingsWindow
from new_project_window import Ui_newProjectWindow
from edit_project_window import Ui_editProjectWindow
from edit_project_window_2 import Ui_editProjectWindow2
from edit_project_window_3 import Ui_editProjectWindow3
from edit_project_window_4
