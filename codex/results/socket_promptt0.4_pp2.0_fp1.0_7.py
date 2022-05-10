import socket
# Test socket.if_indextoname()

import socket
import unittest
from test import support

class TestIfIndextoname(unittest.TestCase):
    def test_if_indextoname(self):
        if_indextoname = socket.if_indextoname
        try:
            if_indextoname(1)
        except OSError as e:
            self.assertEqual(e.errno, errno.ENXIO)
        else:
            self.fail('Expected OSError')

def test_main():
    support.run_unittest(TestIfIndextoname)


if __name__ == "__main__":
    test_main()
