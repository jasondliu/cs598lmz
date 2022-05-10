import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import PyQt5 classes
from PyQt5 import QtCore, QtGui, QtNetwork, QtWebKit, QtWebKitWidgets, QtWidgets

# Import application modules
from gui.mainwindow import MainWindow
import gui.utils

# Import python modules
import os
import sys

# Main entry point
def main():
    """
    Main entry point
    """
    # Create the Qt Application
    app = QtWidgets.QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Run the main Qt loop
    sys.exit(app.exec_())

# Main entry point
if __name__ == '__main__':
    main()
