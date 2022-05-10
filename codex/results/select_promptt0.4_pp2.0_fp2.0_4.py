import select
# Test select.select() on a socketpair

import select
import os
import sys

def test(r, w, e, timeout):
    print 'testing', r, w, e, timeout
    r, w, e = select.select(r, w, e, timeout)
    print 'returned', r, w, e

# Create a pair of connected sockets
if sys.platform == 'win32':
    # On Windows, socketpair() only works on AF_INET sockets
    # So we create an AF_INET socket, bind it, and then do an
    # accept() on it.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('localhost', s.getsockname()[1]))
    s = s.accept()[0]
else:
    s, c = socket.socketpair()

# Set blocking mode on the
