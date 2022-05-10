import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import sys

from . import window

def main():
    app = QApplication(sys.argv)
    w = window.MainWindow()
    w.show()
    sys.exit(app.exec_())
