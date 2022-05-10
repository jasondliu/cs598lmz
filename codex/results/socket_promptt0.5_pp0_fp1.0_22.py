import socket
# Test socket.if_indextoname()

import unittest
import os
import subprocess
import sys
import time
import socket
import fcntl
import struct
import errno

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        for i in range(256):
            try:
                name = socket.if_indextoname(i)
            except OSError as e:
                if e.errno != errno.ENXIO:
                    raise
            else:
                # print(i, name)
                self.assertTrue(name is not None)
                self.assertTrue(isinstance(name, str))
                self.assertTrue(len(name) > 0)

if __name__ == '__main__':
    unittest.main()
