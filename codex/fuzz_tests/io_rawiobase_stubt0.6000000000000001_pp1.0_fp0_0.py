import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        l = len(b) # We're supposed to return at most this much
        chunk = self.file.read(l)
        n = len(chunk)
        b[:n] = chunk
        self.offset += n
        return n

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 1:
            offset += self.offset
        elif whence == 2:
            offset += len(self.file.getvalue())
        self.offset = offset
        return self.offset

    def tell(self):
        return self.offset

    def readable(self):
        return True

# from https://github.com/python/cpython/blob/3.6/Lib/io.py
# -*- coding: utf-8 -*-
#

