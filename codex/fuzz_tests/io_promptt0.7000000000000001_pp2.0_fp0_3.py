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

import test.support

if sys.platform == 'win32' and _winapi:
    class _MemoryIO(_winapi.SafeHandle, io.RawIOBase):
        """Raw I/O implementation for Windows using memory mapped files."""


        def __init__(self, buffer=None, size=0):
            if buffer is not None:
                if isinstance(buffer, bytearray):
                    buffer = bytes(buffer)
                elif isinstance(buffer, str):
                    buffer = memoryview(buffer.encode('utf-8'))
                elif isinstance(buffer, memoryview):
                    buffer = buffer.cast('B')
                else:
                    raise TypeError("buffer must be a bytes-like object")
            if size < 0
