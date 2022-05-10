import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# TODO: Fix this
# sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))

from PySide import QtGui, QtCore

import lib.utilities as utilities

from GUI.mainwindow import MainWindow
from GUI.connectiondialog import ConnectionDialog
from GUI.loggingwindow import LoggingWindow

import lib.constants as constants

__author__ = 'Stefan Hechenberger <stefan@nortd.com>'


class Application(QtGui.QApplication):

    def __init__(self, sys_argv):
        super(Application, self).__init__(sys_argv)

        # main window
        main_window = MainWindow(self.tr("Laserweb"))
        # main_window.show()

        # logging window
        logging_window = LoggingWindow(self.tr("Logging"))
        # logging_window.show()

        # connection window

