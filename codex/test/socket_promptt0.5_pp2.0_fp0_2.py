import socket
# Test socket.if_indextoname() on linux

import unittest
from test.support import requires, requires_linux_version

requires_linux_version(2, 4)
requires('ifconfig')

class IfconfigTest(unittest.TestCase):

    def test_if_indextoname(self):
        # This test is Linux specific
        for i in range(100):
            try:
                ifname = socket.if_indextoname(i)
            except OSError:
                pass
            else:
                self.assertTrue(ifname, "interface name is empty")
                self.assertEqual(i, socket.if_nametoindex(ifname),
                    "interface name to index conversion failed")


if __name__ == "__main__":
    unittest.main()
