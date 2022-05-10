import io
# Test io.RawIOBase class
# See https://docs.python.org/3.5/library/io.html#raw-i-o-classes

import os
import sys

from io import RawIOBase

class FileLike(RawIOBase):
    """
    File-like object that can be used to replace sys.stdin.
    """
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')

    def read(self, size=-1):
        return self.file.read(size)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return self.file.seekable()

    def seek(self, pos, whence=os.SEEK_SET):
        return self.file.seek(pos, whence)

    def tell(self):
        return self.file.tell()

