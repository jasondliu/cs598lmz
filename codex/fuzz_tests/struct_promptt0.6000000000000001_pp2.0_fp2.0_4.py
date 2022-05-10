import _struct
# Test _struct.Struct
def test_struct():
    s = _struct.Struct('bBhHiIlLqQfd')
    print(s.pack(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.0, 12.0))
    print(s.unpack(s.pack(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.0, 12.0)))
    print(s.size)
    print(s.format)

# Test _struct.error
def test_error():
    try:
        _struct.error
    except NameError:
        print("NameError")
    else:
        try:
            raise _struct.error
        except _struct.error:
            print("_struct.error")

# Test _struct.pack, _struct.unpack, _struct.calcsize, _struct.pack_into, _struct.unpack_from
def test_pack_unpack():
    data = _struct.pack('hil', 1, 2, 3)
    print(data)
