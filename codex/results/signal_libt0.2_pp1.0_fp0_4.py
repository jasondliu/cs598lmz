import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from .mainwindow import MainWindow
from . import config

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtMaze")
    app.setOrganizationName("QtMaze")
    app.setOrganizationDomain("qt-maze.org")
    app.setApplicationVersion(config.VERSION)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
