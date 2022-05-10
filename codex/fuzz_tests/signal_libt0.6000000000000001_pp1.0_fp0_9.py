import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebEngineView(QWebView):

    def __init__(self, parent=None):
        super(WebEngineView, self).__init__(parent)

        self.setPage(WebEnginePage(self))
        self.setAcceptDrops(False)

    def createWindow(self, wintype):
        return self.parent().createWindow(wintype)

    def contextMenuEvent(self, event):
        event.preventDefault()
        event.ignore()

    def dropEvent(self, event):
        event.preventDefault()
        event.ignore()

    def dragEnterEvent(self, event):
        event.preventDefault()
        event.ignore()

    def dragMoveEvent(self, event):
        event.preventDefault()
        event.ignore()

    def dragLeaveEvent(self, event):
        event.preventDefault()
        event.ignore()


