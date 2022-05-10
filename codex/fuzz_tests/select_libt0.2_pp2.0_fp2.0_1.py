import select
import socket
import sys
import threading
import time
import traceback

import paramiko

from . import common
from . import config
from . import constants
from . import exceptions
from . import log
from . import utils
from . import version

# pylint: disable=too-many-public-methods
class SSHClient(object):
    """
    A class representing an SSH client.

    :param str hostname: The server to connect to.
    :param str username: The username to authenticate as.
    :param str password: The password to authenticate with.
    :param int port: The port to connect to.
    :param str private_key_file: An optional private key to use for
        authentication.
    :param str private_key_pass: An optional password to use with the private
        key.
    :param float timeout: The timeout in seconds for commands to complete.
    :param bool keep_alive: Send SSH keepalive packets every 60 seconds.
    :param int keep_alive_interval: The interval in seconds for keepalive
        packets
