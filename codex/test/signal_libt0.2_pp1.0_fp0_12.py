import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

from .mainwindow import MainWindow
from . import config

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtWebKit Browser")
    app.setOrganizationName("QtWebKit")
    app.setOrganizationDomain("qtwebkit.org")
    app.setApplicationVersion(config.version)

    mainWindow = MainWindow()
    mainWindow.show()

    if len(sys.argv) > 1:
        mainWindow.load(QUrl(sys.argv[1]))

    sys.exit(app.exec_())
