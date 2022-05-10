import selectors
from selectors import EVENT_READ, EVENT_WRITE

from opentracing.ext import tags

from ..tracer import get_tracer
from ..utils import get_coroutine_name


class TracedBaseServer(socketserver.BaseServer):
    def __init__(self, tracer, server_address, RequestHandlerClass, bind_and_activate=True):
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        self.tracer = tracer
        self.server_address = server_address
        self.server_port = server_address[1]
        self.RequestHandlerClass = RequestHandlerClass

        self.__is_shut_down = threading.Event()
        self.__serving = False

        if self.timeout is None:
            self.timeout = 1

        self.selector = selectors.DefaultSelector()

    def server_activate(self):
        self.socket.listen(self.request_queue_size)

        # Add the server socket to the selector.
        self.selector.
