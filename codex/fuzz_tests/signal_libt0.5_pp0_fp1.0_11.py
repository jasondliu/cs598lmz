import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QTextEdit
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QFileDialog
from PyQt5.QtWidgets import QComboBox, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
import os

from gui.main_window import Ui_MainWindow
from gui.about_window import Ui_AboutWindow
from gui.help_window import Ui_HelpWindow
from gui.settings_window import Ui_SettingsWindow
from gui.comparing_window import Ui_ComparingWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(Q
