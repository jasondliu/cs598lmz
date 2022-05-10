import socket
import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from client.client_ui import Ui_MainWindow
from client.client_thread import ClientThread
from client.client_window import ClientWindow
from client.client_window_list import ClientWindowList
from client.client_window_list_item import ClientWindowListItem
from client.client_window_list_item_ui import Ui_ClientWindowListItem


class Client(QMainWindow):
    def __init__(self, host, port):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.host = host
        self.port = port

        self.client_thread = ClientThread(self.host, self.port)
        self.client_thread.start()

        self.client_thread.message_received.connect(self.on_message_received)
        self.client_thread
