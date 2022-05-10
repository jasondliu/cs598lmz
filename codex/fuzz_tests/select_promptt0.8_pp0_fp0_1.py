import select
# Test select.select
from select import select
r, w, e = select([], [], [], 0.1)
assert r == w == e == [], "select failed"
# Test select.__doc__
from test_support import verbose
if verbose:
    import select
    doc = select.__doc__
    if not doc:
        print "no docstring in select module"
# Test select.select.__doc__
from test_support import verbose
if verbose:
    import select
    doc = select.select.__doc__
    if not doc:
        print "no docstring in select.select"

# Test "fd" arguments
import select
from socket import socket
sock = socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.bind(sock.getsockname())
sock2.listen(1)
r, w, e = select.select([sock2], [], [], 0.1)
assert r == [
