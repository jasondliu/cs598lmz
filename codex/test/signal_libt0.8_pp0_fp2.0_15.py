import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QIcon
import sys
from .main import MainWindow
from .util import getIcon, getResource


def show_main_window(argv=[]):
    # Re-write sys.argv to include any Qt specific options
    sys.argv = [''] + argv[1:]
    # Qt Application creation
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
    app.setWindowIcon(getIcon('icon_app.png'))
    app.setOrganizationName("OpenClinic")
    app.setOrganizationDomain("openclinic.org")
    app.setApplicationName("OpenClinic")

    # Qt Translation
