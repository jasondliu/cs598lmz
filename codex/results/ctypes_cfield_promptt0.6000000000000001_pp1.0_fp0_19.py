import ctypes
# Test ctypes.CField

def test_cfield():
    class Test(ctypes.LittleEndianStructure):
        _fields_ = [("x", ctypes.c_int)]

    t = Test(0)
    assert t.x == 0
    assert Test.x.offset == 0
    assert Test.x.size == 4
    assert Test.x.type is ctypes.c_int
    assert Test.x.index == 0
    assert Test.x.pack == 1
    assert Test.x.readonly is False
    assert Test.x.bitsize is None
    assert Test.x.bitoffset is None
    assert Test.x.type_ == ctypes.c_int
    assert Test.x.name == "x"

    t = Test(1)
    assert t.x == 1
    assert Test.x.offset == 0
    assert Test.x.size == 4
    assert Test.x.type is ctypes.c_int
    assert Test.x.index == 0
    assert Test.x.pack == 1
    assert Test.x.readonly is False
    assert
