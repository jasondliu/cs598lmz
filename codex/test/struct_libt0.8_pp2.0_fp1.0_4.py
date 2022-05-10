import _struct
import setuptools
import sys
import time

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

from . import __version__
from . import bcolors
from . import hash
from . import pbkdf2
from . import ssl
from . import utils

class Client(object):
    """The KDFish client.

    This handles most of the communication to and from the server. It
    provides a number of functions for interacting with KDFish.
    """

    def __init__(self):
        """Initalize KDFish client settings.

        This method attempts to read the KDFish configuration file,
        and will inform the user if anything goes wrong. If there
        is no configuration file, or no entries in the file, the user
        is prompted.
        """

        # Initialize the members.
        self._addr = None
        self._cert = None
        self._conn = None
        self._key  = None
        self._port = None
        self._sock = None

        # Read the configuration file.
