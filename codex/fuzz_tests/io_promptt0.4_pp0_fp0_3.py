import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok

# Helper to test the readinto() method
def readinto_helper(test, rawio, data, buffer_size=None):
    if buffer_size is None:
        buffer_size = len(data)
    b = bytearray(buffer_size)
    n = rawio.readinto(b)
    test.assertEqual(n, len(data))
    test.assertEqual(b[:n], data)

# Helper to test the read() method
def read_helper(test, rawio, data, buffer_size=None):
    if buffer_size is None:
        buffer_size = len(data)
    b = rawio.read(buffer_size)
    test.assertEqual(b, data)

# Helper to test the write() method
def write_helper(test, rawio, data):
    n = rawio.write(data)

