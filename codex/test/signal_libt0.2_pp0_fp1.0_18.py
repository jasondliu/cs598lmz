import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt5.QtWidgets import QApplication

from . import mainwindow

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Casa")
    app.setOrganizationDomain("casa.nrao.edu")
    app.setApplicationName("CasaViewer")
