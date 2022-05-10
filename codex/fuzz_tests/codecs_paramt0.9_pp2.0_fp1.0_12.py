import codecs
codecs.register_error("strict", codecs.ignore_errors)

logging.basicConfig(
    format="%(asctime)-15s [%(levelname)7s] %(filename)s:%(lineno)3d %(message)s",
    level=logging.INFO)

class WebSocketLogHandler(logging.Handler):
    """A logging handler that sends to a websocket."""

    global_websocket_server = WebSocketServer("", 0, "", "", "")
    global_websocket_server.start()
    global_websocket_server.host = "localhost"

    def __init__(self, path, level=logging.NOTSET):
        logging.Handler.__init__(self, level)
        self.counter = 0
        self.path = path
        self.ws = create_connection("ws://%s:%s%s" % (self.global_websocket_server.host, self.global_websocket_server.port, self.path))

    def mapLogRecord(self, record):
        """
