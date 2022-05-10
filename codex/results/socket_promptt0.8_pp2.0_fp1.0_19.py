import socket
# Test socket.if_indextoname()

import unittest
from test.support import run_unittest

interface_name = 'lo'

class InterfaceNameTests(unittest.TestCase):

    def test_valid_interface_name(self):
        self.assertEqual(socket.if_indextoname(1, interface_name),
                         interface_name)

def test_main():
    run_unittest(InterfaceNameTests)

if __name__ == '__main__':
    test_main()
