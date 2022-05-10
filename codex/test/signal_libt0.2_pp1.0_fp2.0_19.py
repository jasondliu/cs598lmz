import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import main_window
from . import config

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtSSTV")
    app.setOrganizationName("QtSSTV")
    app.setOrganizationDomain("qtsstv.org")
    app.setApplicationVersion(config.VERSION)
    window = main_window.MainWindow()
    window.show()
    sys.exit(app.exec_())
