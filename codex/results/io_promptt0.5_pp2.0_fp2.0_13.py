import io
# Test io.RawIOBase.readinto() with a non-empty buffer.

import io
from test.support import run_unittest
from test.support.script_helper import assert_python_ok

from collections import namedtuple
from io import BytesIO
from itertools import chain
import os
import sys
import tempfile

from test.support.script_helper import assert_python_ok

from test.support.script_helper import assert_python_ok

from test.support.script_helper import assert_python_ok

from test.support.script_helper import assert_python_ok

from test.support.script_helper import assert_python_ok

from test.support.script_helper import assert_python_ok

class TestRawIOBaseReadinto:

    def test_readinto(self):
        # Test readinto() with a non-empty buffer
        b = bytearray(b' ' * 100)
        n = self.io.readinto(b)
        self.assertEqual(n, len(self.data))
       
