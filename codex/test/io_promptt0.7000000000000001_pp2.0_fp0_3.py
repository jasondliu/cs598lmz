import io
# Test io.RawIOBase with a memoryview as a writable buffer.
import io
import _io
import mmap
import os
import sys
import tempfile
import unittest
try:
    import mmap
except ImportError:
    mmap = None
try:
    import _winapi
except ImportError:
    _winapi = None

