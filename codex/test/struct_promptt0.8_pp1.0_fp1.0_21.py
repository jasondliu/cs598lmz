import _struct
# Test _struct.Struct interface
# This is not the _struct module's test suite.  This test is for Python code
# that uses the _struct module.

import test.test_support as support

# Format characters that should raise _struct.error.
bad_format_chars = "bBhHiIlLqQfdspPXxUu"

# Format characters that should raise struct.error, but not _struct.error.
bad_bytes_format_chars = "fdsp"

for f in bad_format_chars:
    try:
        _struct.Struct(f)
    except _struct.error:
        pass
    except struct.error:
        pass
    else:
        raise TestFailed("format character '%s' should raise _struct.error" % f)


def test_byteswap():
    s = _struct.Struct("<I")
    if s.unpack_from(s.pack(0x01020304), 0)[0] != 0x01020304:
        raise TestFailed("no byteswap")
    s = _struct.Struct
