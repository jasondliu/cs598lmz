import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import logging

logging.basicConfig(format='%(asctime)s %(message)s')

log = logging.getLogger(__name__)

log.setLevel(logging.INFO)


class WebSocketNotifier(QObject):
    def __init__(self, url, parent=None):
        super(WebSocketNotifier, self).__init__(parent)
        self.url = url
        self.add_header = 'upstream'

        self.sock = QWebSocket()
        self.sock.connected.connect(self.on_connected)
        self.sock.disconnected.connect(self.on_disconnected)
        self.sock.textFrameReceived.connect(self.on_textframe_received)

        self.sock.open(QUrl(self.url))

    def on_connected(self):
        log.info("WebSocket connected.")

