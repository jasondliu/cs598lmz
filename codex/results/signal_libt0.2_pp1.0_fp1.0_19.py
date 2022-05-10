import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from .main_window import MainWindow
from . import config

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName(config.ORGANIZATION_NAME)
    app.setOrganizationDomain(config.ORGANIZATION_DOMAIN)
    app.setApplicationName(config.APPLICATION_NAME)
    app.setApplicationVersion(config.APPLICATION_VERSION)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
