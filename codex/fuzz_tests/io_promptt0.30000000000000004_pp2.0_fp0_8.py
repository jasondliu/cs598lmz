import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import import_helper
from test.support.script_helper import assert_python_ok

# Issue #7995: check that io.RawIOBase.readinto() is usable
# from Cython
HERE = os.path.dirname(__file__) or os.curdir
src = os.path.join(HERE, "readinto.pyx")
code = import_helper.load_source("readinto", src)

# Issue #7995: check that io.RawIOBase.readinto() is usable
# from Cython
HERE = os.path.dirname(__file__) or os.curdir
src = os.path.join(HERE, "readinto.pyx")
code = import_helper.load_source("readinto", src)

class MyRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0


