import socket
# Test socket.if_indextoname()

from test.support import verbose, run_unittest
import unittest
from test.support import socket_helper

class IfIndextonameTest(unittest.TestCase):
    def test_if_indextoname(self):
        ifname = socket.if_indextoname(socket_helper.get_if_index())
        if verbose:
            print('ifname:', ifname)
        self.assertTrue(ifname)
        self.assertTrue(isinstance(ifname, str))


def test_main():
    run_unittest(IfIndextonameTest)


if __name__ == "__main__":
    test_main()
