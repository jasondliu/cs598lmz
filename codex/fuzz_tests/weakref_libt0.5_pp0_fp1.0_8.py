import weakref

from .. import utils
from .. import constants


class Client(object):
    """
    This is the main class used to interact with the server.
    It provides access to the public methods of the server.
    """

    def __init__(self, host, port, username, password, use_ssl=False,
                 ssl_verify=True, timeout=60, alias=None):
        """
        :param host: Hostname or IP address of the server.
        :type host: str
        :param port: Port number of the server.
        :type port: int
        :param username: Username to use for authentication.
        :type username: str
        :param password: Password to use for authentication.
        :type password: str
        :param use_ssl: Whether to use SSL/TLS or not.
        :type use_ssl: bool
        :param ssl_verify: Whether to verify the SSL/TLS certificate or not.
        :type ssl_verify: bool
        :param timeout: Timeout for the connection in seconds.
        :type timeout:
