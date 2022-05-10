import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from . import mainwindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Qt5-WebApp")
    app.setOrganizationName("Qt5-WebApp")
    app.setOrganizationDomain("qt5-webapp.org")
    app.setApplicationVersion("0.1")

