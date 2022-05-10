import weakref
import sys
import netifaces as ni
import ipaddress as ipa
import time

from numpy import array


class NetworkScanner(QWidget):
    """Main window of the controller
    """
    def __init__(self, parent=None):
        super(NetworkScanner, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setMinimumSize(600, 600)
        self.setWindowTitle("Network scanner")
