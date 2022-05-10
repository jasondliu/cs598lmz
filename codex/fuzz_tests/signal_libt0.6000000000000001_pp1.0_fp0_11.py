import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from mainwindow import MainWindow
from settings import Settings

from version import version
from utils import load_stylesheet

from gettext import gettext as _
from gettext import bindtextdomain, textdomain

textdomain(Settings.name)
bindtextdomain(Settings.name, Settings.locale_dir)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName(Settings.org_name)
    app.setApplicationName(Settings.name)
    app.setApplicationVersion(version)
    app.setWindowIcon(QIcon(':/icon.png'))
    app.setStyleSheet(load_stylesheet())

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
