import _struct
# Test _struct.Struct.unpack_from

# Some large number that's not a power of two.
N = 15
value = _struct.unpack_from('H', b'\0' * N)[0]
assert value == 0

value = _struct.unpack_from('H', b'\0' * (N + 1))[0]
assert value == 0
