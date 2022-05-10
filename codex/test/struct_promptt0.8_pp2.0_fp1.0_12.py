import _struct
# Test _struct.Struct.format_size(), which should work
# exactly like struct.calcsize(), and its module-level
# equivalent, _struct.calcsize().
from _inttest_support import format_size_tests

for fmt, size in format_size_tests:
    assert _struct.Struct(fmt).format_size() == size
    assert _struct.calcsize(fmt) == size
