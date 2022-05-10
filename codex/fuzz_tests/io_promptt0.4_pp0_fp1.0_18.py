import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    # File-like object that reads and writes to a list of strings.
    class ListIO(io.RawIOBase):

        def __init__(self, lst):
            self._lst = lst

        def readinto(self, b):
            if not self._lst:
                return None
            data = self._lst[0]
            del self._lst[0]
            n = len(b)
            if len(data) > n:
                b[:n] = data[:n]
                self._lst.insert(0, data[n:])
            else:
                b[:len(data)] = data
            return len(data)

        def write(self, b):
            self._lst.append(bytes(b))
            return len(b)

    def test_constructor(self):
        # No args
        io.RawIOBase()
        # Explicit

