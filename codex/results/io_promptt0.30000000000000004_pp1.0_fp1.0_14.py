import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

# Base class for testing RawIOBase
class BaseRawIO(io.RawIOBase):
    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        data = self.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array) or err.args[0] != "buffer is read-only":
                raise
            b[:n] = array.array("b", data)
        return n

    def write(self, b):
        self.write_stack.append(b)
        return len(b)

    def seek(self, pos, whence=0):
        if whence == 0:
            self.seek_pos = pos
        elif whence == 1:
            self.seek_pos +=
