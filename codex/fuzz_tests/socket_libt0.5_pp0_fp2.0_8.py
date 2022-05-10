import socket
import json
import time
import sys
import threading
import traceback
import random

from . import message
from . import exceptions
from . import constants
from . import utils

class Client(object):
    """
    Client class for connecting to a rosbridge server and sending/receiving messages.

    :param str host: hostname or ip address of the rosbridge server
    :param int port: port number of the rosbridge server
    :param str id: optional id to use for the client
    :param int timeout: optional timeout for socket operations
    :param bool disable_signatures: disable message signatures in the header
    :param bool compression: enable compression in the header
    """

    def __init__(self, host, port, id=None, timeout=None, disable_signatures=False, compression=False):
        self.host = host
        self.port = port
        self.id = id or utils.generate_id()
        self.timeout = timeout
        self.socket = None
        self.connected = False
        self.disable_signatures = disable
