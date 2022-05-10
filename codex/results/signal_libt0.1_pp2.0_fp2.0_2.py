import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from .main_window import MainWindow
from . import __version__


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtPyVCP")
    app.setApplicationVersion(__version__)
    app.setOrganizationName("QtPyVCP")
    app.setOrganizationDomain("qtpyvcp.org")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
