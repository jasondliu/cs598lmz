import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

from . import mainwindow
from . import settings
from . import utils
from . import updater
from . import version
from . import __appname__


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName(__appname__)
    app.setApplicationName(__appname__)
    app.setApplicationVersion(version.VERSION)
    app.setWindowIcon(QIcon(utils.get_resource_path('icons/icon.png')))

    settings.load()
    main_window = mainwindow.MainWindow()
    main_window.show()

    if settings.get('check_for_updates'):
        QTimer.singleShot(0, updater.check_for_updates)

    sys.exit(app.exec_())
