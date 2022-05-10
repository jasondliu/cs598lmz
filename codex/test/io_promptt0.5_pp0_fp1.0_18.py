import io
# Test io.RawIOBase
#
# This test covers the RawIOBase interface, which deals with low-level
# unbuffered I/O.
#
# The tests are constructed so as to be able to run this test file directly,
# for debugging.

import io
import os
import sys
import unittest
from io import UnsupportedOperation
