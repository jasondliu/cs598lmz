import select
# Test select.select on a pair of sockets using pollable and
# non-pollable interfaces

import unittest

try:
    import socket
    import time
    import errno
    import sys
    import os
    import select
    import io
    import signal
    import pty
    try:
        import threading as _threading
    except ImportError:
        import dummy_threading as _threading
except ImportError:
    # not all platforms built with socket module
    raise unittest.SkipTest("can't import socket module")

# Silence is golden
def close_sockets(s):
    for s in s:
        try:
            if s is not None:
                s.close()
        except socket.error:
            pass

class PollableTest(unittest.TestCase):

    def setUp(self):
        self.svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.svr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

