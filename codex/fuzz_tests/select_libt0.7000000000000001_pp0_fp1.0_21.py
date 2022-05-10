import select
import socket
from contextlib import contextmanager

from .logger import logger
from .utils import net


class InStream(object):
    """
    Base class for input stream
    """
    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self._closed = False
        self._buffer = b''

    def _read_from_socket(self, sock, n):
        """
        Read n bytes from socket, used internally
        """
        future = asyncio.Future(loop=self.loop)

        def on_readable():
            try:
                future.set_result(sock.recv(n))
            except Exception as e:
                future.set_exception(e)

        self.loop.add_reader(sock, on_readable)
        return future

    @contextmanager
    def ctx(self):
        yield self

    async def read(self, n=-1):
        """
        Read n bytes from stream
        """
        if self._closed:
            return
