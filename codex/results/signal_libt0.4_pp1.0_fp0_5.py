import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtGui import QApplication

from . import __version__
from .main_window import MainWindow
from .utils import get_icon


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtPip")
    app.setApplicationVersion(__version__)
    app.setWindowIcon(get_icon("qtpiplogo"))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
