import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Main Window')

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.init_menu()

    def init_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')

       
