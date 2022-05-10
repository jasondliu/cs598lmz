import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QHBoxLayout, QVBoxLayout, QGridLayout, QMessageBox, QDialog)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from main_window import MainWindow
from login_window import LoginWindow
from register_window import RegisterWindow
from about_window import AboutWindow
from settings_window import SettingsWindow
from add_window import AddWindow
from edit_window import EditWindow
from delete_window import DeleteWindow
from database import Database

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Password Manager')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300,
