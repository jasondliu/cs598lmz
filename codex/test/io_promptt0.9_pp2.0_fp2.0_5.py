import io
# Test io.RawIOBase.readinto

# Example from the docs.

import io, os, sys

class File:
    def __init__(self, file, mode='r'):
        self._file = file
        self._pos = self._file.tell()
        self._line = 0
    def __iter__(self):
        return self
    def next(self):
        line = self._file.readline()
        if not line:
            self._file.seek(self._pos)
            raise StopIteration
        self._line += 1
        return " %3d:  %r" % (self._line, line)

