import _struct
# Test _struct.Struct
def max_align():
    return _struct.calcsize('P')

def pack_test():
    # pack
    s = _struct.Struct('i')
    packed = s.pack(1)
    assert packed == b'\x01\x00\x00\x00'
    packed = s.pack(1, 2)
    assert packed == b'\x01\x00\x00\x00'
    packed = s.pack(1, 2, 3)
    assert packed == b'\x01\x00\x00\x00'
    s = _struct.Struct('Q')
    packed = s.pack(1)
    assert packed == b'\x01\x00\x00\x00\x00\x00\x00\x00'
    packed = s.pack(1, 2)
    assert packed == b'\x01\x00\x00\x00\x00\x00\x00\x00'
    packed = s.pack(1, 2, 3)
    assert packed == b'\x
