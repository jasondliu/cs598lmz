import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QWidget

class WebPage(QWebEnginePage):
    def acceptNavigationRequest(self, url, type, isMainFrame):
        if isMainFrame and type == QWebEnginePage.NavigationTypeLinkClicked:
            self.view().setUrl(url)
            return False
        return True

class Browser(QWebEngineView):
    def __init__(self):
        # QWebEngineView
        self.view = QWebEngineView.__init__(self)
        #self.setPage(WebPage(self))
        self.setWindowTitle('Loading...')
        self
