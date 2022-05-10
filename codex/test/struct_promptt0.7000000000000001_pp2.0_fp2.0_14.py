import _struct
# Test _struct.Struct
import struct

# Test struct.Struct*
import struct

# Test struct.pack_into
def f(s):
    import struct
    return struct.pack_into("c", b"", 0, s)

# Test struct.unpack_from
def f(s):
    import struct
    return struct.unpack_from("c", s, 0)

# Test _struct.pack_into
def f(s):
    import _struct
    return _struct.pack_into("c", b"", 0, s)

# Test _struct.unpack_from
def f(s):
    import _struct
    return _struct.unpack_from("c", s, 0)

# Test struct.Struct.pack_into
def f(s):
    return struct.Struct("c").pack_into(b"", 0, s)

# Test struct.Struct.unpack_from
def f(s):
    return struct.Struct("c").unpack_from(s, 0)

# Test _struct.Struct.pack_into
