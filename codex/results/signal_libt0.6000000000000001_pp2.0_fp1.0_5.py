import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWebKit import QWebSettings
import bs4 as bs
import urllib.request
import urllib
import lxml
import re
import time
import pandas as pd
import numpy as np

class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        
    def on_page_load(self):
        self.app.quit()
        
def main():
    url = 'https://www.boxofficemojo.
