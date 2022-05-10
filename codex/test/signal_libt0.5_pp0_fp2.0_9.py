import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QTimer

class MainWindow(QWebEngineView):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Test")
        self.setGeometry(0, 0, 800, 600)
        self.load(QUrl("http://www.google.com"))

        self._channel = QWebChannel(self)
        self.page().setWebChannel(self._channel)
        self.page().loadFinished.connect(self._on_load_finished)

