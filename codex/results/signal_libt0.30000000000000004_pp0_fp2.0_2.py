import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import __version__, __author__
from .gui import MainWindow
from . import utils


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Mosaic')
    app.setApplicationVersion(__version__)
    app.setOrganizationName(__author__)
    app.setOrganizationDomain('github.com/juanpabloaj/mosaic')
    app.setWindowIcon(utils.get_icon('mosaic'))
    app.setStyle('Fusion')

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
