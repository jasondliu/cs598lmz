import io
# Test io.RawIOBase
# ------------------------------------------------------------------------

# io.RawIOBase is an abstract base class for implementing Raw I/O.
# See the close(), read(), readinto(), write() and seek() methods for
# more information.
print('--- io.RawIOBase ---')
class TestRawIO(io.RawIOBase):

    def read(self, n=None):

        # Implements raw reading from the object. The n argument is
        # the number of bytes to read. Reads should return at most
        # n bytes. Less than n bytes may be returned if the end of
        # the file or stream is reached.
        print('read({})'.format(n))
        return None

    def write(self, b):

        # Implements raw writing to the object. The b argument can be
        # any object supporting the buffer protocol.
        print('write({})'.format(b))
        return None

print('--- TestRawIO() ---')
r = TestRawIO()
r.read()
r.read(None)
r.read(1)
r.read(1.1)

