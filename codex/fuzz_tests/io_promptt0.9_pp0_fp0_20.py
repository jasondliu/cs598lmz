import io
# Test io.RawIOBase
import pickle
import codecs

import unittest
from test import support

class MyRawIO(io.RawIOBase):
    def __init__(self, s):
        self._s = s
        self._i = 0

    def close(self):
        pass
    def fileno(self):
        raise NotImplementedError
    def flush(self):
        pass
    def isatty(self):
        return False
    def readable(self):
        return True
    def readline(self, limit=-1):
        i = self._i
        if limit < 0:
            j = len(self._s)
        else:
            j = min(i + limit, len(self._s))
        try:
            nl = self._s.index('\n', i, j)
        except ValueError:
            nl = j
        ret = self._s[i:nl]
        self._i = nl + 1
        return ret

    def seekable(self):
        return True
    def seek(self, pos, whence
