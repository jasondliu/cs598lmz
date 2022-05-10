import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from . import __version__
from . import config
from . import gui
from . import logic
from . import resources


def main(args=None):
    app = QApplication(args or [])
    app.setApplicationName('QtPass')
    app.setApplicationVersion(__version__)
    app.setWindowIcon(QIcon(':/icons/qtpass.svg'))

    # Make sure the config is initialized before the GUI
    config.init(app.applicationName())

    # Create GUI and logic
    main_window = gui.MainWindow()
    logic = logic.Logic(main_window)

    # Connect GUI signals
    main_window.set_password_store.connect(logic.set_password_store)
    main_window.refresh_password_store.connect(log
