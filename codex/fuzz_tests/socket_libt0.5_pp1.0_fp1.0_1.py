import socket
from threading import Thread

from PyQt5.QtCore import QThread, pyqtSignal

from Client.client import Client
from Client.gui.main_window import MainWindow
from Client.gui.sign_up_window import SignUpWindow
from Client.gui.login_window import LoginWindow
from Client.gui.chat_window import ChatWindow


class Gui:
    def __init__(self):
        self.client = Client()
        self.app = QApplication(sys.argv)
        self.login_window = LoginWindow()
        self.login_window.show()
        self.sign_up_window = SignUpWindow()
        self.main_window = MainWindow()
        self.chat_window = ChatWindow()
        self.chat_window.hide()
        self.main_window.hide()
        self.sign_up_window.hide()
        self.login_window.log_in_button.clicked.connect(self.log_in)
        self.login_window.sign_up_button.clicked.connect(self
