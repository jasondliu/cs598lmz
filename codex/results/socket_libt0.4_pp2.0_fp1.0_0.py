import socket
import traceback
import time

from collections import defaultdict

from . import constants
from . import utils
from . import packet
from . import protocol

from .protocol import Protocol
from .packet import Packet
from .constants import *
from .utils import *

from . import logger

class Client(object):
    """
    A client to connect to a Minecraft server.

    :param str address: The server address.
    :param int port: The server port.
    :param str username: The username to login with.
    :param str password: The password to login with.
    :param str client_token: The client token to login with.
    :param str access_token: The access token to login with.
    :param bool offline: Whether to login in offline mode.
    :param str version: The version of Minecraft to login with.
    :param str server_info: The server info to login with.
    :param int protocol_version: The protocol version to use.
    """

    def __init__(self,
                 address,
                 port,
                 username
