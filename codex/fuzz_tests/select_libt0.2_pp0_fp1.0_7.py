import select
import socket
import sys
import time

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The maximum number of bytes to read from a socket at one time:
MAX_BYTES = 65536

#-------------------------------------------------------------------------------
#  'Socket' class:
#-------------------------------------------------------------------------------

class Socket:
    """ Represents a socket connection. """

    #---------------------------------------------------------------------------
    #  Initializes the object:
    #---------------------------------------------------------------------------

    def __init__ ( self, host, port ):
        """ Initializes the object.
        """
        self.host = host
        self.port = port
        self.socket = None
        self.connected = False
        self.connect()

    #---------------------------------------------------------------------------
    #  Closes the socket connection:
    #---------------------------------------------------------------------------

    def close ( self ):
        """ Closes the socket connection.
        """
        if self.connected:
            self.socket.close()
            self.connected = False

    #---------------------------------------------------------------------------
    #  Connects to the socket:
    #---------------------------------------------------------------------------

    def connect ( self ):
        """ Connects to the socket
