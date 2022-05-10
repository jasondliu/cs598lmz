import selectors
import signal
import sys
import traceback

# Default timeout for the selectors forwarder in seconds
DEFAULT_TIMEOUT = 10

# Default buffer size when reading from a socket
BUFFER_SIZE = 65536


class IncompleteRead(Exception):
    """Read did not read to the end of the socket."""


class TimeoutError(Exception):
    """Timeout error."""


class Forwarder:
    """Handles the forwarding of bytes between two sockets."""

    def __init__(self, client_sock, server_sock, timeout=DEFAULT_TIMEOUT):
        """
        Initialize a new forwarder instance.

        Args:
            client_sock: The client socket.
            server_sock: The server socket.
            timeout: Timeout in seconds that the forwarder will wait
                     before giving up reading. It will attempt again
                     after this time if there is still data to read.
        """
        self.client_sock = client_sock
        self.server_sock = server_sock
        self.timeout = timeout
        self
