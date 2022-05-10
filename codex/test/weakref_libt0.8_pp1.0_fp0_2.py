import weakref

WEBSERVER_IP = "127.0.0.1"
WEBSERVER_PORT = "8080"

class WebsocketServer(object):
    """docstring for WebsocketServer"""
    config = {}
    handler = None
    handler_instance = None

    def __init__(self, cfg):
        super(WebsocketServer, self).__init__()
        self.config = cfg

        try:
            self.handler = cfg["class"]
            self.handler_instance = self.handler(cfg)
        except Exception as err:
            print("Error loading websocket handler {}".format(err))

    def startServer(self):
        print("Starting websocket server on {}:{}".format(WEBSERVER_IP, WEBSERVER_PORT))
        self.start_server = websockets.serve(self.handler_instance.start, WEBSERVER_IP, WEBSERVER_PORT)
        asyncio.get_event_loop().run_until_complete(self.start_server)
        asyncio.get_
