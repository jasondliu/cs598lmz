import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings

from . import __version__
from .mainwindow import MainWindow


def main():
    app = QApplication([])
    app.setOrganizationName("Clement Pit-Claudel")
    app.setOrganizationDomain("clement.pitclaudel.com")
    app.setApplicationName("Qt-based Python REPL")
    app.setApplicationVersion(__version__)
    app.setWindowIcon(QIcon(":/icons/python.png"))
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app.setAttribute(Qt.AA_DontShowIconsInMenus)

    settings = QSettings()
    window = MainWindow(settings)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
