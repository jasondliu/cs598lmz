import _struct
# Test _struct.Struct.format itself.
s = _struct.Struct('h')
s.format
s = _struct.Struct('hh')
s.format
s = _struct.Struct('hhh')
s.format
s = _struct.Struct('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
s.format
# Issue #15007: Test that Struct.format does not cause an
# arbitrary-precision integer overflow.
def mangle_int(x):
    return x ^ 0x12345678
s = _struct.Struct(mangle_int(28))
def test_format(fmt):
    s = _struct.Struct(fmt)
    return s.format
# Ensure that test_format() returns a string of the expected size,
# without an "arbitrary-precision" overflow.
def check_format_len(fmt, len):
    f = test_format(fmt)
    return len(f) == len
# Count how many tests we run, and how many failed.
ntests = 0
nfail = 0
import sys
maxint = sys.maxsize
while
