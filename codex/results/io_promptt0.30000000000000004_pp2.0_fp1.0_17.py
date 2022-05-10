import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import bigmemtest
from test.support.script_helper import assert_python_ok

# Test RawIOBase using a StringIO object

class TestRawIO(io.RawIOBase):

    def __init__(self, buf=b''):
        self._buf = buf
        self._pos = 0

    def read(self, n=-1):
        newpos = self._pos + n
        if newpos < 0:
            newpos = 0
        r = self._buf[self._pos:newpos]
        self._pos = newpos
        return r

    def write(self, b):
        if self._pos == len(self._buf):
            self._buf += b
            self._pos += len(b)
            return len(b)
        newpos = self._pos + len(b)
        if newpos > len(self._buf):
            newpos = len(self._buf)
        self._buf = self._buf[:self._
