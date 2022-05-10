import socket
import sys

from . import exceptions
from . import utils

DEFAULT_SOCKET_TIMEOUT = 5
DEFAULT_RETRY_COUNT = 3
DEFAULT_RETRY_INTERVAL = 3


class Client(object):
    """
    Client for the ClickHouse HTTP interface.
    """

    def __init__(self, host='localhost', port=8123, database=None, user=None, password=None,
                 socket_timeout=DEFAULT_SOCKET_TIMEOUT):
        """
        Initializes the client.

        :param host: The hostname of the ClickHouse server.
        :param port: The port of the ClickHouse server.
        :param database: The default database.
        :param user: The default user.
        :param password: The default password.
        :param socket_timeout: The socket timeout.
        """
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.socket_timeout = socket_timeout

    def execute(self
