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
        self.setStyleSheet(
            "QPushButton {"
            "background-color: #336699;"
            "color: #ffffff;"
            "border-radius: 10px;"
            "border-style: outset;"
            "border-width: 2px;"
            "border-color: #6600ff;"
            "padding: 6px;"
            "}"
            "QPushButton:pressed {"
            "background-color: #663399;"
            "border-style: inset;"
            "}"
            "QPushButton:hover {"
            "background-color
