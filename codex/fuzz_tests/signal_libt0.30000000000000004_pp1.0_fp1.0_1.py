import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

from .mainwindow import MainWindow
from .config import Config
from . import __version__

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtWebBrowser")
    app.setOrganizationName("QtWebBrowser")
    app.setApplicationVersion(__version__)

    config = Config()
    window = MainWindow(config)
    window.show()

    if len(sys.argv) > 1:
        QUrl.fromUserInput(sys.argv[1])
    else:
        window.tabwidget.loadHome()

    sys.exit(app.exec_())
