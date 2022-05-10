import select
# Test select.select() on a socket

import select
import socket
import time

def test(args=None):
    if args is None:
        args = sys.argv[1:]

    if sys.platform == "win32":
        print "XXX no select test on win32"
        return

    # Make sure select.select doesn't crash on a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    s2, addr = s.accept()
    s.close()

    # Try reading
    r, w, x = select.select([s2], [], [], 0.1)
    if r:
        raise RuntimeError, "socket should be unreadable"
    # Try writing
    r, w, x = select.select([], [s2], [], 0.1)
    if w:
        raise RuntimeError, "socket should be unwriteable"
    # Try exceptional condition
    r, w, x = select.select([], [],
