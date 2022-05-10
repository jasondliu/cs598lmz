import _struct
# Test _struct.Struct

def test(typecode):
    sz = _struct.calcsize(typecode)
    fmt = _struct.Struct(typecode)
    data = (1, 2, 3, 4)
    buf = fmt.pack(*data)
    assert len(buf) == sz
    assert fmt.size == sz

    unpacked = fmt.unpack(buf)
    assert unpacked == data, (unpacked, data)

    fmt = _struct.Struct(typecode + 'i')
    data = (1, 2, 3, 4, 5)
    buf = fmt.pack(*data)
    assert len(buf) == sz + _struct.calcsize('i')
    assert fmt.size == sz + _struct.calcsize('i')

    unpacked = fmt.unpack(buf)
    assert unpacked == data, (unpacked, data)

    fmt = _struct.Struct(typecode + typecode)
    data = (1, 2, 3, 4, 1, 2, 3, 4)
    buf = fmt.pack(*data)
   
