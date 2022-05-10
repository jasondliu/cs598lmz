import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from . import __appname__, __version__
from .widgets.mainwindow import MainWindow


def main():
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    app = QApplication(sys.argv)
    app.setApplicationName(__appname__)
    app.setApplicationVersion(__version__)
    app.setWindowIcon(QIcon(':/icons/icon.png'))
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
