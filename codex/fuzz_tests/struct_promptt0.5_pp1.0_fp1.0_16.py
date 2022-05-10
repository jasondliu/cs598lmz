import _struct
# Test _struct.Struct

## _struct.Struct

s = _struct.Struct("b")
s = _struct.Struct("b", _struct.LITTLE_ENDIAN)
s = _struct.Struct("b", _struct.BIG_ENDIAN)
s = _struct.Struct("b", _struct.NATIVE_ENDIAN)
s = _struct.Struct("b", _struct.NETWORK_ENDIAN)

## _struct.Struct.__init__

s = _struct.Struct("b")
s = _struct.Struct("b", _struct.LITTLE_ENDIAN)
s = _struct.Struct("b", _struct.BIG_ENDIAN)
s = _struct.Struct("b", _struct.NATIVE_ENDIAN)
s = _struct.Struct("b", _struct.NETWORK_ENDIAN)

## _struct.Struct.format

s = _struct.Struct("b")
assert s.format == "b"

## _struct.Struct.size

s = _struct.Struct("b")
assert s.size == 1

## _struct.
