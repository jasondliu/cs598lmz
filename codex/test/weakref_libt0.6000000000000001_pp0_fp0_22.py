import weakref
import logging
import time
import threading

from tornado.ioloop import IOLoop
from tornado.iostream import IOStream

from ..messages import Message, Notify, Query, Response
from ..errors import *

class Client(object):
    """
    Client for a remote Horde server.

    Typically, you will want to use :meth:`connect` to connect to the server,
    then use the :attr:`notify` and :attr:`query` methods to send requests.

    You can also use :attr:`send` to send arbitrary messages.

    :param io_loop: The IOLoop to use.
    :param address: The address to connect to.
    :param port: The port to connect to.
    """

    def __init__(self, io_loop=None, address='127.0.0.1', port=9000):
        self._logger = logging.getLogger('horde.client')

        self._io_loop = io_loop or IOLoop.instance()

        self._sock = None
