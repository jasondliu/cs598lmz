import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import mainwindow
from . import config

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QtMidi")
    app.setOrganizationName("QtMidi")
    app.setOrganizationDomain("qtmidi.org")
    app.setApplicationVersion(config.VERSION)
    app.setStyle("Fusion")

    window = mainwindow.MainWindow()
    window.show()

    sys.exit(app.exec_())
