import _struct
import _socket

#
# Class to handle the TCP/IP communication with the server.
#
class TCPHandler(object):

    #
    # Initialize the TCP/IP handler.
    #
    def __init__(self, server_ip, server_port, buffer_size=1024):

        self._server_ip = server_ip
        self._server_port = server_port
        self._buffer_size = buffer_size
        self._socket = None
        self._connected = False

    #
    # Connect to the server.
    #
    def connect(self):

        self._socket = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
        self._socket.connect((self._server_ip, self._server_port))
        self._connected = True

    #
    # Disconnect from the server.
    #
    def disconnect(self):

        self._socket.close()
        self._connected = False

    #
    # Check if the connection is established.
    #
    def is_connected(self):


