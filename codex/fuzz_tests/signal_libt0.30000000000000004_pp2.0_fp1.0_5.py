import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import __version__
from .main_window import MainWindow
from . import config


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtVk")
    app.setOrganizationName("QtVk")
    app.setOrganizationDomain("https://github.com/vk-qt/QtVk")
    app.setApplicationVersion(__version__)

    main_window = MainWindow()
    main_window.show()

    config.load()

    sys.exit(app.exec_())
