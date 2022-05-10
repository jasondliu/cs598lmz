import _struct
# Test _struct.Struct

# Test the basic methods

s = _struct.Struct('i')

assert s.size == _struct.calcsize('i')
assert s.format == 'i'

assert s.pack(1) == b'\x01\x00\x00\x00'
assert s.unpack(b'\x01\x00\x00\x00') == (1,)

# Test the keyword arguments

s = _struct.Struct('i', True)
assert s.size == _struct.calcsize('i')
assert s.format == '!' + 'i'

assert s.pack(1) == b'\x00\x00\x00\x01'
assert s.unpack(b'\x00\x00\x00\x01') == (1,)

s = _struct.Struct('i', False)
assert s.size == _struct.calcsize('i')
assert s.format == 'i'

assert s.pack(1) == b'\x01\x00\x00\x00'
assert
