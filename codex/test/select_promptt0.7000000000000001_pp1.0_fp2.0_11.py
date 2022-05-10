import select
# Test select.select() on a non-blocking socket

import errno
import socket

from test.support import get_attribute, run_unittest, TESTFN
run_unittest(__name__)

HOST = 'www.python.org'
PORT = 80

# IMPORTANT:  This test assumes that the machine is not running any proxy
# server.  If you are behind a firewall, then you might have to disable this
# test.

def test_select():
    # First try to connect to www.python.org. If we can't connect to the
    # socket, then skip the test.
    try:
        s = socket.socket()
        s.connect((HOST, PORT))
    except OSError as exc:
        # On OS X, this is not a socket error.
        if exc.errno != get_attribute(errno, 'ECONNREFUSED'):
            raise unittest.SkipTest(
                'cannot connect to %s:%d: %s' % (HOST, PORT, exc))
        raise
    s
