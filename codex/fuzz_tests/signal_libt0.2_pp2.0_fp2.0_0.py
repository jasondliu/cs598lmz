import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import QThread, pyqtSignal, QObject

import sys

class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.run)

    def run(self):
        print("Thread started")
        self.finished.emit()
        print("Thread finished")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Start thread")
        self.label = QLabel("Thread not started")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout
