import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt4 import QtGui

from . import main_window

def main():
    app = QtGui.QApplication(sys.argv)
    window = main_window.MainWindow()
    window.show()
    sys.exit(app.exec_())
