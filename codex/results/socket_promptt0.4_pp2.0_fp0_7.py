import socket
# Test socket.if_indextoname()

from test.support import run_unittest, TESTFN, unlink
from test.support.script_helper import assert_python_ok
import unittest
import os

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # The test is not reliable, because it depends on the network
        # configuration of the machine.  It is mainly useful to check
        # that the function doesn't crash.
        try:
            socket.if_indextoname(1)
        except OSError:
            pass

def test_main():
    run_unittest(IfIndextonameTestCase)
    # Check that socket.if_indextoname() is available
    script = """if 1:
        import socket
        socket.if_indextoname(1)
        """
    assert_python_ok('-c', script)

if __name__ == '__main__':
    test_main()
