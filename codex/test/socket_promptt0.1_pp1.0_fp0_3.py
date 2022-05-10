import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # This test is not very good, but it's better than nothing.
        # It assumes that there is at least one interface on the system.
        # It also assumes that the first interface has a name of at least
        # two characters.
        name = socket.if_indextoname(1)
        self.assertTrue(name)
        self.assertTrue(len(name) >= 2)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
