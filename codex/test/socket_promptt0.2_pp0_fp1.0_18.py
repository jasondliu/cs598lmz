import socket
# Test socket.if_indextoname()

import os, sys
import unittest
from test import support

try:
    socket.if_indextoname(1)
except OSError as err:
    if err.errno == errno.EOPNOTSUPP:
        raise unittest.SkipTest("platform lacks required functionality")
    raise

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test socket.if_indextoname()
        # We can't test much, but we can at least check that it
        # doesn't crash, and that it accepts valid input.
        try:
            socket.if_indextoname(1)
        except OSError as err:
            if err.errno == errno.EINVAL:
                # Invalid index
                pass
            else:
                raise

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
