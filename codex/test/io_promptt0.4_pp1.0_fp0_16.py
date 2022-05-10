import io
# Test io.RawIOBase
#
# This test checks that io.RawIOBase is a working base class for raw I/O.
# It does so by deriving a RawIO subclass and performing various file-like
# operations on it.  If any of the operations fail, an exception will be
# raised, and the test should fail.

class TestRawIO(io.RawIOBase):

    def __init__(self, data):
        self._data = data
        self._pos = 0

    def read(self, n=None):
        if n is None:
            newpos = len(self._data)
        else:
            newpos = min(self._pos + n, len(self._data))
        b = self._data[self._pos:newpos]
        self._pos = newpos
        return b

    def write(self, b):
        newpos = self._pos + len(b)
        if newpos > len(self._data):
            raise IOError('out of bounds')
