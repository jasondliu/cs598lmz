import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from .main_window import MainWindow
from . import __version__


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Guitar Pro Tabs')
    app.setApplicationVersion(__version__)
    app.setOrganizationName('Guitar Pro Tabs')
    app.setOrganizationDomain('guitarprotabs.info')

    main_window = MainWindow()
    main_window.show()

    # Для поддержки темы оформления приложения, которую можно задать в настройках
    # для все
