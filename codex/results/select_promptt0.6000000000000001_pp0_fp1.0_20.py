import select
# Test select.select()
#
# Usage: test_select.py
#
# This program uses select.select() to implement a simple
# line-at-a-time chat server.
#
# Any number of clients can connect to the server.
# The server echoes each line of input back to each client.
#
# The server exits gracefully when a client sends an empty line.
#
# A client exits gracefully when the server sends an empty line.
#
# To test the server, run this program and then telnet to port 12345.
#
# Example:
#
#   $ python test_select.py
#   $ telnet localhost 12345
#
# When the server is running, telnet to port 12345 to see the echo.
#

# The port on which the server listens
PORT = 12345

# The number of seconds to wait when listening for new connections
TIMEOUT = 60

class ChatServer(object):
    """
    A simple line-at-a-time chat server, using select.select()
    """
    def __init__(self, port):
        """

