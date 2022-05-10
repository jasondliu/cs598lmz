import selectors
import sys
import traceback

#-------------------------------------------------------------------------------
#   Constants
#-------------------------------------------------------------------------------

# The port that the server will be listening on
SERVER_PORT = 65432

# The maximum number of bytes that can be sent or received in a single message
MAX_MSG_SIZE = 1024

#-------------------------------------------------------------------------------
#   Server
#-------------------------------------------------------------------------------

# Create a selector
sel = selectors.DefaultSelector()

# Create a server socket
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind(('', SERVER_PORT))
lsock.listen()
print('listening on', (lsock.getsockname()))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

#-------------------------------------------------------------------------------
#   Main Loop
#-------------------------------------------------------------------------------

