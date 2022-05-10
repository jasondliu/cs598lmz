import _struct
# Test _struct.Struct
struct = _struct.Struct('>hhl')
x = struct.pack(1, 2, 3)
struct.unpack(x)

# Test _struct.calcsize
_struct.calcsize('>hhl')

# Test _struct.error
try:
    _struct.error
except NameError:
    print("SKIP")
    raise SystemExit


# Test _struct.pack
_struct.pack('>hhl', 1, 2, 3)

# Test _struct.pack_into
import array
buf = array.array('b', b'\0' * _struct.calcsize('>hhl'))
_struct.pack_into('>hhl', buf, 0, 1, 2, 3)

# Test _struct.unpack
_struct.unpack('>hhl', b'\0\1\0\2\0\0\0\3')

# Test _struct.unpack_from
buf = array.array('b', b'\0\1\0\2\0\0\0\3')
_struct
