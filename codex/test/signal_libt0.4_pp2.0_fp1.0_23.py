import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

class WebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super(WebPage, self).__init__(parent)
        self.profile().setHttpCacheType(QWebEngineProfile.NoCache)

    def acceptNavigationRequest(self, url, type, isMainFrame):
        if type == QWebEnginePage.NavigationTypeLinkClicked:
            self.load(url)
            return False
        return True

class Browser(QWebEngineView):
    def __init__(self):
        self.view = QWebEngineView.__init__(self)
