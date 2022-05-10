import socket
import threading

from yaml import load
from yaml import Loader

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from pyparsing import Group, Literal, Word, Optional, ZeroOrMore, OneOrMore, Forward, alphas, nums, alphanums, QuotedString, dblQuotedString, restOfLine
from pyparsing import Combine, White, Suppress, LineEnd, ParseException

from . import config
from . import log
from . import util
from . import system
from . import connection
from . import protocol
from . import group
from . import user

class Server(object):
    """
    The server class
    """

    def __init__(self, configFile = None):
        """
        Constructor

        Keyword arguments:
        configFile -- The file to load the server configuration from (default None)
        """

        # Set the default configuration
        self.config = config.Config(configFile)

        # Setup the logger
        self.logger
