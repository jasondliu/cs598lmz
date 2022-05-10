import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt4 import QtGui, QtCore

from carta import CARTA
from carta.ui.gui import MainWindow


def main():
    """
    Run the CARTA GUI.
    """
    app = QtGui.QApplication(sys.argv)
    app.setStyle('plastique')
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
