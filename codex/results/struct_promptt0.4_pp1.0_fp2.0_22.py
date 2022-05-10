import _struct
# Test _struct.Struct.

# Test with a simple format string.
s = _struct.Struct('i')

# Test with a format string that uses 'p' and 'P'.
# These are only supported on 64-bit platforms.
if _struct.calcsize('P') == 8:
    s = _struct.Struct('PiP')

# Test with a format string that uses a size.
s = _struct.Struct('10s')

# Test with a format string that uses a size and alignment.
s = _struct.Struct('@10s')

# Test with a format string that uses a size, alignment, and native byte-order.
s = _struct.Struct('=10s')

# Test with a format string that uses a size, alignment, and standard size.
s = _struct.Struct('@=10s')

# Test with a format string that uses a size, alignment, and standard size,
# and native byte-order.
s = _struct.Struct('=@10s')

# Test with a format string that uses a size, alignment, and standard size,
# and standard byte
