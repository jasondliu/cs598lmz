import socket
import sys
import threading
import time
import traceback
from xml.etree import ElementTree

import requests
import zmq

from . import config
from . import log
from . import utils

logger = log.getLogger(__name__)


class ZmqHandler(logging.Handler):
    """A logging handler that sends log messages over a 0MQ socket.

    """
    def __init__(self, socket_url):
        logging.Handler.__init__(self)
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.connect(socket_url)

    def emit(self, record):
        try:
            self.socket.send(self.format(record))
        except Exception:
            self.handleError(record)


class ZmqListener(threading.Thread):
    """A thread that listens for log messages published over a 0MQ socket.

    """
