import io
# Test io.RawIOBase.readable() method

class RawIOBase_readable(io.RawIOBase):
    def readable(self):
        return False         # Cannot read

try:
    f = RawIOBase_readable()
    f.read()
except IOError, e:
    if e.errno != errno.EBADF: raise
else:
    raise AssertionError
