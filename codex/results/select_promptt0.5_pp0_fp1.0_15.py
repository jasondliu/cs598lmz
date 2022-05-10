import select
# Test select.select() with a simple case.

import select
import socket
import sys
import time

def test(timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 80))
    s.setblocking(0)
    rl, wl, xl = select.select([s], [], [], timeout)
    s.close()
    return rl, wl, xl

# Test that select() returns an empty list if the timeout is 0.
rl, wl, xl = test(0)
assert len(rl) == 0
assert len(wl) == 0
assert len(xl) == 0

# Test that select() returns an empty list if the timeout is negative.
rl, wl, xl = test(-1)
assert len(rl) == 0
assert len(wl) == 0
assert len(xl) == 0

# Test that select() returns an empty list if the timeout is None.
rl, wl, xl = test(None)
assert len(rl)
