import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
from PyQt4 import QtGui, QtCore
from qtdesigner import Ui_MainWindow


class MainUi(QtGui.QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup buttons
        self.ui.button_1.clicked.connect(lambda: self.button_clicked(self.ui.button_1))
        self.ui.button_2.clicked.connect(lambda: self.button_clicked(self.ui.button_2))
        self.ui.button_3.clicked.connect(lambda: self.button_clicked(self.ui.button_3))
        self.ui.button_4.clicked.connect(lambda: self.button_clicked(self.ui.button_4))
        self.ui.button
