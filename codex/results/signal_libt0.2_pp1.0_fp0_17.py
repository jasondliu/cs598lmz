import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from . import mainwindow
from . import settings
from . import utils
from . import resources

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Coderus")
    app.setOrganizationDomain("coderus.ru")
    app.setApplicationName("Sailfish Connect")
    app.setApplicationVersion(utils.get_version())
    app.setWindowIcon(resources.icon("sailfish-connect.png"))

    settings.load()

    window = mainwindow.MainWindow()
    window.show()

    # Workaround for https://github.com/sailfishos/sailfish-silica/issues/8
    QTimer.singleShot(0, window.update_ui)

    sys.exit(app.exec_())
