import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from . import main_window
from . import config
from . import settings
from . import utils


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Lantern")
    app.setOrganizationName("Lantern")
    app.setOrganizationDomain("getlantern.org")

    # Load settings
    settings.load()

    # Load config
    config.load()

    # Create main window
    window = main_window.MainWindow()

    # Show main window
    window.show()

    # Start update timer
    timer = QTimer()
    timer.timeout.connect(window.update)
    timer.start(1000)

    # Run application
    sys.exit(app.exec_())
