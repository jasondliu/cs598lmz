import _struct
# Test _struct.Struct
try:
    _struct.Struct('i').size
except ValueError:
    # Issue #1258: _struct.Struct(format) does not accept a unicode string
    pass
else:
    raise Exception
# Test struct.calcsize
try:
    struct.calcsize('i')
except ValueError:
    # Issue #1258: struct.calcsize(format) does not accept a unicode string
    pass
else:
    raise Exception

# Issue #1712
if not hasattr(sys, 'gettotalrefcount'):
    print("SKIP")
    raise SystemExit

import _testcapi

# Memory leaks in test_capi?

def test():
    # We are trying to leak references in the test_capi module, which
    # means we're running under a debug build of Python.  So we need
    # to use sys.gettotalrefcount() to check for leaks.
    import gc
    gc.collect()
    n = sys.gettotalrefcount()

    # Some functions that should not leak references
