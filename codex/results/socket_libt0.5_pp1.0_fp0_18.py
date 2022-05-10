import socket
import sys
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from mainwindow import MainWindow


class App(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.main_window = MainWindow()
        self.main_window.show()
        self.start_timer()

    def start_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.ping)
        self.timer.start(1000)

    def ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect(('127.0.0.1', 65432))
            self.main_window.status_bar.showMessage('Connected')
            s.close()
        except socket.error:
            self.main_window.status_bar.showMessage('Disconnected')

