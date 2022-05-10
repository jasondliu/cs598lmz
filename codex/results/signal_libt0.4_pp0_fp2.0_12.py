import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import mainwindow
from . import settings
from . import utils

def main():
    app = QApplication(sys.argv)
    app.setApplicationName('QtPass')
    app.setOrganizationName('IJHack')
    app.setOrganizationDomain('ijhack.org')
    app.setStyle('Fusion')
    app.setWindowIcon(utils.icon('qtpass'))
    settings.load()
    window = mainwindow.MainWindow()
    window.show()
    sys.exit(app.exec_())
