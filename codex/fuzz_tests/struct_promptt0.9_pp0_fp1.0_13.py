import _struct
# Test _struct.Struct.p.  Part of python-3605.

import struct
import _struct
from test import support

# Some fun and games with _struct.Struct.p

# Sample data
SAMPLE_DATA = (b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00')

# Unpack
class UnpackTest(tuple):
    def __new__(cls, fmt, source):
        self = super(UnpackTest, cls).__new__(cls, struct.unpack(fmt, source))
        self.fmt = fmt
        self.source = source
        return self
    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.fmt, self.source)

tests = [
    UnpackTest('LLLL', SAMPLE_DATA),      # Big-endian integers using standard
    UnpackTest('
