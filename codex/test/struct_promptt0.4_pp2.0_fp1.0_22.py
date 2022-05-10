import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('x')
    except TypeError:
        pass
    else:
        print('TypeError expected')

def test_struct_size():
    s = _struct.Struct('i')
    if s.size != 4:
        print('size of i should be 4, not', s.size)

def test_struct_pack_error():
    s = _struct.Struct('i')
    try:
        s.pack()
    except TypeError:
        pass
    else:
        print('TypeError expected')

def test_struct_pack_unpack():
    s = _struct.Struct('i')
    packed = s.pack(12345)
    if packed != b'\x39\x30\x00\x00':
        print('pack(12345) should return b"\\x39\\x30\\x00\\x00", not',
              packed)
    unpacked = s.unpack(packed)
