import select
# Test select.select() to see if it's working
import time
import sys

# Create a pair of connected sockets
if len(sys.argv) != 2:
    print >>sys.stderr, 'Usage: select_echo_server.py <port>'
    sys.exit(2)

port = int(sys.argv[1])

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Avoid bind() exception: OSError: [Errno 48] Address already in use
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lsock.bind(('', port))
lsock.listen()
