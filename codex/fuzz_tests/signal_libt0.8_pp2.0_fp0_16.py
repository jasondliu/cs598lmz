import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import qrc_resources

# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QVariant', 2)

import design

class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # Connect up the buttons.
        self.btnBrowse.clicked.connect(self.browse_folder)

    def browse_folder(self):
        directory = QFileDialog.getExistingDirectory(self,
                "Find Files", QDir.currentPath())

        if directory:
            if self.txtBrowse.text() != directory:
                self.
