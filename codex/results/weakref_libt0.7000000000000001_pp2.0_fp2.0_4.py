import weakref

from PyQt5.QtCore import pyqtSignal, QObject

from . import get_qapplication
from .qparsedurl import QParsedUrl

class QUrlReceiver(QObject):
    url_received = pyqtSignal(QParsedUrl)
    #url_received = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._url_received = self.url_received.emit

        # connect to the drop_url_received signal of the QApplication
        self._qapplication = get_qapplication()
        self._qapplication.url_received.connect(self._url_received)
        self._qapplication_ref = weakref.ref(self._qapplication)

    def receive_urls(self):
        """
        Start listening for URLs
        """
        self._qapplication.receive_urls()

    def stop_receiving_urls(self):
        """
        Stop listening for URLs
        """
        self._q
