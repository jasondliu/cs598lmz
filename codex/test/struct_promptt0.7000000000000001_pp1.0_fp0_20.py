import _struct
# Test _struct.Struct with a non-native format
try:
    _struct.Struct('@')
except TypeError:
    pass
else:
    raise TestFailed('Expected TypeError, did not get one')

# test struct packing and unpacking
try:
    struct.pack('ccc', b'A', b'\xfe', b'\xff')
except struct.error:
    raise TestFailed('invalid char in struct format')
else:
    raise TestFailed('expected struct.error, did not get one')

try:
    struct.pack('hhh', 1, 2, 3)
except struct.error:
    raise TestFailed('invalid char in struct format')
else:
    raise TestFailed('expected struct.error, did not get one')

try:
    struct.pack('hhh', 1, 2)
except struct.error:
    raise TestFailed('invalid char in struct format')
