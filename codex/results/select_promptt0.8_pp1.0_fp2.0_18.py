import select
# Test select.select() on non-blocking sockets; this should always be
# immediately ready to read and write.
import signal
import os

from test.support import run_unittest, socket_helper, reap_children, is_jython, HOST, unlink

# Skip the following tests if AF_UNIX is not available.
if not hasattr(socket, 'AF_UNIX'):
    raise unittest.SkipTest("AF_UNIX is not available on this platform")

# Skip the following tests if AF_INET6 is not available and
# if sockets.has_ipv6 is False.
if not hasattr(socket, 'AF_INET6') and not socket.has_ipv6:
    raise unittest.SkipTest("IPv6 is not available on this platform")

# Skip the following tests if AF_TIPC is not available.
if not hasattr(socket, 'AF_TIPC'):
    raise unittest.SkipTest("AF_TIPC is not available on this platform")

if (select.select([], [], [], 0)
