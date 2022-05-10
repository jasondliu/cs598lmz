import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok

# Test RawIOBase using a StringIO object

class TestRawIO(io.RawIOBase):

    def __init__(self, buf=""):
        self.buf = buf
        self.len = len(buf)
        self.readall = False

    def readable(self):
        return True

    def seekable(self):
        return True

    def writable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            newpos = pos
        elif whence == 1:
            newpos = self.pos + pos
        elif whence == 2:
            newpos = self.len + pos
        else:
            raise ValueError("whence must be 0, 1 or 2")
        if newpos < 0:
            raise ValueError("new position is negative")
        self.pos = newpos
        return
