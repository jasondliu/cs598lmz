import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl

import vlc

from ui_mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    """Main Window inherits QMainWindow"""
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(1)

        self.player = vlc.MediaPlayer()

        self.makeConnections()

    def makeConnections(self):
        self.ui.playButton.clicked.connect(self.play)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui
