import io
# Test io.RawIOBase subclasses that are not file-like.
# Issue #21007: io.RawIOBase subclasses read(), readinto() and readall()
# should be allowed to return a short read.

import errno
import io
import os
import sys
import unittest
import unittest.mock
