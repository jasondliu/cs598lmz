import _struct
# Test _struct.Struct
assert _struct.Struct('i').pack(1) == b'\x01\x00\x00\x00'
assert _struct.Struct('i').pack(1, 2, 3) == b'\x01\x00\x00\x00'
assert _struct.Struct('i').unpack(b'\x01\x00\x00\x00') == (1,)
assert _struct.Struct('i').unpack(b'\x01\x00\x00\x00' * 2) == (1, 1)
# Test _struct.error
try:
    _struct.error
except NameError:
    print('SKIP')
    import sys
    sys.exit()
try:
    _struct.Struct('x').unpack(b'')
except _struct.error:
    print('_struct.error')
# Test _struct.Struct('!i').__sizeof__()
assert _struct.Struct('!i').__sizeof__() == 4
# Test _struct.Struct(b'i').pack_into()
data = bytear
