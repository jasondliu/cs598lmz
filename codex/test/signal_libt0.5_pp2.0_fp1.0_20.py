import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon

from . import __version__
from .mainwindow import MainWindow
from . import resources_rc


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("MangaDownloader")
    app.setApplicationVersion(__version__)
    app.setOrganizationName("MangaDownloader")
    app.setOrganizationDomain("https://github.com/MangaDownloader/MangaDownloader")
    app.setWindowIcon(QIcon(":/icons/manga.png"))
    app.setQuitOnLastWindowClosed(True)

    settings = QSettings()

    mainWindow = MainWindow(settings)
    mainWindow.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
