import io
# Test io.RawIOBase
#
# This tests the RawIOBase implementation of the io module.  Since
# RawIOBase is a base class, the tests are performed by creating a
# number of derived classes.
#
# Note that RawIOBase derives from IOBase, which is tested in test_io.
# The tests for open(), close(), seek(), tell(), truncate(), read(),
# readinto(), write() and detach() are therefore not repeated here.

import io
import os
import sys
import tempfile
import unittest
from io import BytesIO, StringIO
