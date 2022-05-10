import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

from . import __version__
from .mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtWebEngine")
    app.setApplicationVersion(__version__)
    app.setOrganizationName("QtWebEngine")
    app.setOrganizationDomain("qtwebengine.org")

    window = MainWindow()
    window.show()

    if len(sys.argv) > 1:
        window.load(QUrl(sys.argv[1]))

    sys.exit(app.exec_())
