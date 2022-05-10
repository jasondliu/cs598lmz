import io
# Test io.RawIOBase
# an example of how to inherit io.RawIOBase

class MyRawIO(io.RawIOBase):
    def __init__(self, data = None):
        self._data = data or 'abcdefgh'
        self._pos = 0
    def readable(self):
        return True
    def readinto(self, b):
        if self._pos >= len(self._data):
            return None
        b[:3] = self._data[self._pos:self._pos+3]
        self._pos += 3
        return 3
    def write(self, b):
        pass

try:
    from fd_io import FdRawIO
except ImportError:
    pass
else:
    class TestFdRawIO(unittest.TestCase):
        def test_read(self):
            with io.open(__file__, "rb") as testf:
                fd_rawio = FdRawIO(testf.fileno(), closefd=False)
                fio_data = fd_rawio.read()
