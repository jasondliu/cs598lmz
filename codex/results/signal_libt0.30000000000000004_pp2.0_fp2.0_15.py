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
    if config.get('auto_update'):
        QTimer.singleShot(0, window.update)
    sys.exit(app.exec_())
