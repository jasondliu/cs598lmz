import _struct
# Test _struct.Struct
st1 = _struct.Struct("")
assert st1.size == 0
st1 = _struct.Struct("i")
assert st1.size == _struct.calcsize("i")

class MyStruct(_struct.Struct):
    pass

mystruct = MyStruct("i")
assert mystruct.size == _struct.calcsize("i")

# Test that we can find the endianness
def test_bigendian():
    big_endian = _struct.unpack("=i", b'\0\0\0@')[0] == 64
    assert big_endian is _struct.bigendian
    if _struct.unpack("<i", b'\0\0\0@')[0] == 64:
        assert not _struct.bigendian
    else:
        assert _struct.bigendian

# Issue 6926: Struct constructor allows to specify an alternate format
struct_A = _struct.Struct("=i")
struct_B = _struct.Struct("xy", format="=i")
assert struct_A.size == _struct.
