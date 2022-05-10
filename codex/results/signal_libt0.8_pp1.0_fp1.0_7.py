import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from ui_main import Ui_MainWindow
from ui_webview import Ui_Form

from bs4 import BeautifulSoup
import requests
import sys
import time

class WebView(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.link = "https://www.worldometers.info/coronavirus/"
        self.webView.load(QtCore.QUrl(self.link))
        #self.pushButton.clicked.connect(self.load_link)
        self.pushButton.clicked.connect(self.load_link2)

    def load_link(self):
        self.webView.load(QUrl.fromUserInput(self.link))


