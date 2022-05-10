import _struct
import zlib

class _genmagic(object):
    def __init__(self, fd):
        self._fd = fd

    def read(self, size):
        if size > self._fd.length:
            size = self._fd.length
        bs = self._fd.read(size)
        if len(bs) != size:
            raise ValueError("couldn't read all data")
        return bs

class _magic(object):
    # constants
    MAGIC = None
    MAGIC_CHECK = None
    LENGTH = None
    FORMAT = None
    ENDIAN = None

    def __init__(self, fd):
        self._fd = fd
        self.length = self.LENGTH

    def __repr__(self):
        return str(self.MAGIC)

    def read(self, size):
        return self._fd.read(size)

    def seek(self, offset, from_what=os.SEEK_SET):
        return self._fd.seek(offset, from_what)

    def
