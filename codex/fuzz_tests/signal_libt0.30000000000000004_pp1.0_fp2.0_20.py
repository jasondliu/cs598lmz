import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from . import main_window
from . import settings
from . import utils
from . import log
from . import version


def main():
    """Main entry point for the application."""
    app = QApplication(sys.argv)
    app.setApplicationName("TrayIcon")
    app.setOrganizationName("TrayIcon")
    app.setOrganizationDomain("TrayIcon.org")
    app.setApplicationVersion(version.__version__)

    # Load settings
    settings.load()

    # Initialize logging
    log.init()

    # Initialize the main window
    window = main_window.MainWindow()
    window.show()

    # Initialize the tray icon
    tray_icon = window.tray_icon

    # Initialize the update checker
    update_checker = window.update_checker

    # Initialize the
