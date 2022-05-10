import io
# Test io.RawIOBase
import io as _io
try:
    from io import UnsupportedOperation
except ImportError:
    UnsupportedOperation = _io.UnsupportedOperation
# Test _io.BufferedIOBase
# Test _io.BytesIO
# Test _io.FileIO
# Test _io.BytesIO

# try:
#     import _io
# except ImportError:
#     # PyPy doesn't have _io
#     pass
# else:
#     # Test _io.BufferedIOBase
#     # Test _io.BytesIO
#     # Test _io.FileIO
#     # Test _io.BytesIO

# Test buffer
# Test bytes
# Test bytearray
# Test memoryview
# Test array
# Test collections.abc.MutableSequence
# Test list
# Test tuple
# Test range
# Test collections.abc.ItemsView
# Test dict
# Test collections.abc.Mapping
# Test collections.abc.Set
# Test set
# Test frozenset
import itertools
# Test itertools._grouper
# Test itertools
