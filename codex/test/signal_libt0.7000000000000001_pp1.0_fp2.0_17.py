import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Modules
import os
import sys
import time

# PyQt modules
from PyQt4 import QtCore, QtGui

# App modules
from mainwindow import MainWindow

# Application
app = QtGui.QApplication(sys.argv)

# Main window
window = MainWindow()
window.show()

# Execute
app.exec_()
