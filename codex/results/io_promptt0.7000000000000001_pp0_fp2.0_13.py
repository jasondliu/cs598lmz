import io
# Test io.RawIOBase

import io
import sys
import unittest
from test import support

# Test that the attributes exist
io.RawIOBase.name
io.RawIOBase.mode
io.RawIOBase.close
io.RawIOBase.closed
io.RawIOBase.fileno
io.RawIOBase.isatty
io.RawIOBase.flush
io.RawIOBase.readable
io.RawIOBase.readline
io.RawIOBase.readlines
io.RawIOBase.read
io.RawIOBase.seek
io.RawIOBase.seekable
io.RawIOBase.tell
io.RawIOBase.truncate
io.RawIOBase.writable
io.RawIOBase.writelines
io.RawIOBase.write

# Test that the attributes are read-only
def set_name():
    io.RawIOBase().name = "name"
def set_mode():
    io.RawIOBase().mode = "mode"
def set_close():
    io.RawIOBase().close = "close"
def set_closed():
   
