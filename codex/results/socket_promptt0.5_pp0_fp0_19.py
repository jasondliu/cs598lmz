import socket
# Test socket.if_indextoname()
# The test will fail if the function is not present

import unittest
from test import support

class IfIndexTest(unittest.TestCase):

    def test_if_indextoname(self):
        if_name = socket.if_indextoname(1)
        if_index = socket.if_nametoindex(if_name)
        self.assertEqual(if_index, 1)

def test_main():
    support.run_unittest(IfIndexTest)

if __name__ == "__main__":
    test_main()
