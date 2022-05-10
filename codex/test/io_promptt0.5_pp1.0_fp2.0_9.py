import io
# Test io.RawIOBase
try:
    io.RawIOBase.read
except AttributeError:
    import unittest
    raise unittest.SkipTest("test_io requires io.RawIOBase.read()")

import os
import sys
import unittest

