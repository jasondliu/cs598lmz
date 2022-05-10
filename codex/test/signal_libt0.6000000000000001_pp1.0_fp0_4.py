import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.login_widget = LoginWidget(self)
        self.central_widget.addWidget(self.login_widget)
        self.login_widget.login_successful.connect(self.login_successful_slot)
        self.login_widget.register_successful.connect(self.register_successful_slot)
        self.login_widget.login_failure.connect(self.login_failure_slot)

