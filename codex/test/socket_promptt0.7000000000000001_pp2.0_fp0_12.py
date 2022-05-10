import socket
# Test socket.if_indextoname

import os, struct, sys
import unittest
import socket, errno, select

from test.support import TESTFN, run_unittest, reap_children, \
    find_unused_port, bind_port

HOST = '127.0.0.1'

def get_test_ifname():
    """Test a known interface."""
    try:
        return os.environ['TEST_INTERFACE']
    except KeyError:
        pass
    # Try to find an interface that is up, not loopback, not p-to-p,
    # and not point-to-multipoint.
    try:
        f = open('/proc/net/dev', 'r')
    except OSError as err:
        if err.errno == errno.ENOENT:
            raise unittest.SkipTest('cannot read /proc/net/dev')
        raise
