import io
# Test io.RawIOBase as in-memory stream
# See https://docs.python.org/3/library/io.html#io.RawIOBase
# and https://github.com/python/cpython/blob/3.6/Lib/io.py
# and https://docs.python.org/3/library/io.html#example
# and https://github.com/python/cpython/blob/master/Lib/test/test_io.py
# and https://github.com/python/cpython/blob/master/Lib/test/test_io.py#L267
# and https://github.com/python/cpython/blob/master/Lib/test/test_io.py#L279

data = b"abcd"


class InMemoryFile(io.RawIOBase):
    def readable(self):
        return True

    def readinto(self, b):
        read = len(b)
        # The python3 signature is readinto(b: Union[bytearray, memoryview])
        # cast to bytearray to be compatible with python2

