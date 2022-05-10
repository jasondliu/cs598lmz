import _struct
# Test _struct.Struct

# This test does not check the actual values, just
# that the calls don't crash.

def test_struct():
    s = _struct.Struct("i")
    s.unpack_from("xxxxxx")
    s.unpack("xxxxx")
    s.pack(1)
    s.pack_into("xxxx", 1)
    s.calcsize()
    s.size
    s.format

def test_error():
    try:
        s = _struct.Struct("")
    except ValueError:
        pass
