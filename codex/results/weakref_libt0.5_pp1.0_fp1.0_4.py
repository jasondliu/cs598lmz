import weakref

from pymongo import MongoClient
from pymongo.errors import AutoReconnect

from . import config
from . import utils


class Database(object):
    """
    Database wrapper
    """
    def __init__(self, host=None, port=None, database=None,
                 username=None, password=None,
                 auto_reconnect=True, **kwargs):
        """
        :param host: The host to connect to.
        :type host: str
        :param port: The port to connect to.
        :type port: int
        :param database: The database to use.
        :type database: str
        :param username: The username to connect with.
        :type username: str
        :param password: The password to connect with.
        :type password: str
        :param auto_reconnect: Whether to auto reconnect.
        :type auto_reconnect: bool
        """
        self.auto_reconnect = auto_reconnect
        self._client = None
        self._db = None
        self._host = host or config.
