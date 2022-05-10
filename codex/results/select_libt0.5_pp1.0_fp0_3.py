import select
import sys
import time
import traceback
import types

import six

from . import (
    constants,
    exceptions,
    utils,
)


class BaseTransport(object):
    """
    Base transport class.

    :param host: Hostname or IP address of the remote host.
    :param port: Port number of the remote host.
    :param username: Username to authenticate with.
    :param password: Password to authenticate with.
    :param key_filename: Filename of private key to authenticate with.
    :param timeout: Connection timeout.
    """
    def __init__(self, host, port, username, password, key_filename, timeout):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.timeout = timeout

    def connect(self):
        """
        Connect to the remote host.

        :return: Transport layer object.
        """
        raise NotImplementedError

    def close(self):
       
