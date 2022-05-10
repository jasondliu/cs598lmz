import socket
# Test socket.if_indextoname() and socket.if_nametoindex() methods

from test import support
import unittest

class IfconfigTests(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertEqual(socket.if_indextoname(1), 'lo')

    def test_if_nametoindex(self):
        self.assertEqual(socket.if_nametoindex('lo'), 1)


def test_main():
    support.run_unittest(IfconfigTests)


if __name__ == '__main__':
    test_main()
