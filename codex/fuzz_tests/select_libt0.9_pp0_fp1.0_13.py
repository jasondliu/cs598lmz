import selectors
import re



from const import *
from command_interpreter import *
import time
from enum import Enum


class ConnectionType(Enum):
    """ Enum encapulsating the type of a connection
    """
    SOCKET = 1
    SILENTBUTDANGEROUS = 2



# Only use this class if we have no selectionKey to work with
class SilentButDangerous:
    """Class to hide the fact that selectors persist connection objects,
    even those with closed sockets.
    """

    def __init__(self, conn):
        """Initialise me, I don't do nothing.

        Arguments:
           conn {[type]} -- [description]
        """
        assert conn is None
        self.closed = False
        self.sock = None

    def close(self):
        """This is also a noop.
        """
        self.closed = True


class Server:
    """Class representing the server, does all the basic state keeping,
    but delegates to command interpreter the implementing of a command
    """

    def __init
