import socket
# Test socket.if_indextoname
assert socket.if_indextoname(1, None) is None
assert socket.if_indextoname(1, b"") is None
assert socket.if_indextoname(1, b"\0") is None
try:
    socket.if_indextoname(1, b"123456789\01234567")
except ValueError:
    pass
else:
    assert False, "ValueError not raised"

try:
    socket.if_indextoname(65536, b"12345678")
except ValueError:
    pass
else:
    assert False, "ValueError not raised"

import errno
import os
import select

# Test select on a file descriptor that disappear.
r, w = os.pipe()
os.close(r)
assert select.select([r], [], [], 0.0) == ([], [], []), "select with invalid descriptor failed"

# Test select.select() on system that don't support select.
try:
    import select_noop
except ImportError:
    pass

