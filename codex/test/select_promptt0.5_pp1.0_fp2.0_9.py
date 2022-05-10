import select
# Test select.select()
#
# -- LionKimbro 2005-03-19
#

import socket
import select

# This is a "dummy" server, that simply sends a message,
# and then closes the connection.
#
# It should be run from one terminal, and the client should
# be run from a different terminal.
#
# The client should read the message, and then exit.
#
# The server should not exit until the client has closed
# the connection.
#

def server():
    """
    """
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    s.bind(("",12345))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        conn.send("Hello World\n")
        conn.close()

# This is a "dummy" client, that simply connects to the
# server, and then reads a message, and then closes the
# connection.
#
# It should be run from one terminal, and the server should
# be run from a different terminal
