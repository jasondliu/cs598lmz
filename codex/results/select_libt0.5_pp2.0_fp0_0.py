import select
import socket
import struct
import sys

#from daemon import Daemon
from os import path
from time import sleep

from mr_utils import view
from mr_utils.utils import mr_warning
from mr_utils.utils.exceptions import mr_warning_once
from mr_utils.utils.system import is_port_in_use

from .utils import get_ip_address, get_mac_address

class Server(object):
    """
    Server class.

    Parameters
    ----------
    port : int
        Port number to use.
    """

    def __init__(self, port, *args, **kwargs):

        self.port = port

        self.clients = []
        self.sockets = []
        self.ip = ''
        self.mac = ''

        # TODO: Add more robust error handling
        # TODO: Add some way to make sure that the port is free on the host
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server
