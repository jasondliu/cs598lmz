import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets

from . import mainwindow
from . import settings
from . import utils
from . import __version__


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("QtPass")
    app.setOrganizationName("IJHack")
    app.setOrganizationDomain("ijhack.org")
    app.setApplicationVersion(__version__)
    app.setWindowIcon(QtGui.QIcon.fromTheme("qtpass"))
    app.setQuitOnLastWindowClosed(False)

    # load translations
    translator = QtCore.QTranslator()
    translator.load(QtCore.QLocale(), "qtpass", "_", ":/translations")
    app.installTranslator(translator)

    # load settings
    settings.load()

    # create main window
    window = mainwindow.MainWindow()

