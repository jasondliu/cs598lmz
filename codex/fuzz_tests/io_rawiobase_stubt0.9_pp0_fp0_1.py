import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
    def close(self):
        if self.f is not None:
            self.f.close()
            self.f = None
    def fileno(self):
        return self.f.fileno()
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return True
    def tell(self):
        return self.f.tell()
    def seek(self, off, whence=io.SEEK_SET):
        self.f.seek(off, whence)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return self.close()

import struct
import collections
class PackedStruct(object):
    def __init__(self, fmt, doc=None, endian="="
