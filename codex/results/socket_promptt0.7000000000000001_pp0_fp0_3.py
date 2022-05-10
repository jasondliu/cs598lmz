import socket
# Test socket.if_indextoname()

import os, sys
import unittest
from test.support import run_unittest

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        for name in socket.if_nameindex():
            self.assertIsInstance(name[0], int)
            self.assertIsInstance(name[1], str)
            ifname = socket.if_indextoname(name[0])
            self.assertEqual(name[1], ifname)

def test_main():
    run_unittest(IfIndextonameTestCase)

if __name__ == "__main__":
    test_main()
