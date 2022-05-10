import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)  # enable Ctrl-C

from PyQt5 import QtCore, QtGui

from ..gui.mainwindow import MainWindow
from ..core import bands


class Application(QtGui.QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.mainwindow = MainWindow()
        self.mainwindow.show()
        self.mainwindow.resize(1200, 600)
        self.mainwindow.setWindowTitle("SDRplay Spectrum Analyzer")

        # save some preferences and restore them on restart
        self.settings = QtCore.QSettings("SDRplay", "Spectrum Analyzer")
        self.mainwindow.restoreGeometry(
            self.settings.value("geometry", self.mainwindow.saveGeometry()))
        self.mainwindow.restoreState(
            self.settings.value("windowState", self.mainwindow.saveState()))
        self.mainwindow.restoreSplitter(
            self.settings
