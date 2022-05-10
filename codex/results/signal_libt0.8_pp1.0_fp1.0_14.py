import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from artiq.tools import (simple_network_args, init_logger)
from artiq.protocols.pc_rpc import Server


class PCHost(QtCore.QObject):
    @QtCore.pyqtSlot()
    def aboutToQuit(self):
        try:
            self.server.close()
        except AttributeError:
            pass

    def run(self, args):
        init_logger(args)

        app = QtWidgets.QApplication([])
        app.aboutToQuit.connect(self.aboutToQuit)

        host = self.host_from_args(args)
        self.server = Server(host)
       
