import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings

from . import __version__
from .gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("GitHub")
    app.setOrganizationDomain("github.com")
    app.setApplicationName("GitHub Desktop")
    app.setApplicationVersion(__version__)

    settings = QSettings()
    window = MainWindow(settings)
    window.show()

    sys.exit(app.exec_())
