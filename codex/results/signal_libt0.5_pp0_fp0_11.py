import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connections
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionAbout_Qt.triggered.connect(self.aboutQt)
        self.ui.actionLoad.triggered.connect(self.load)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionSave_as.triggered.connect(self.saveAs)
        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionSettings.triggered.
