import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from .mainwindow import MainWindow
from . import config

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(500)
    sys.exit(app.exec_())
