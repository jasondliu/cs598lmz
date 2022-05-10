import ctypes
# Test ctypes.CField
def test_CField():
    # Constructor
    f = ctypes.CField(ctypes.c_char, 'name')
    assert f.name == "name"
    assert f.offset == ctypes.c_char._type_.get_offset(b"name")
    f = ctypes.CField(ctypes.c_int, 'name', 1)
    assert f.name == "name"
    assert f.offset == ctypes.c_int._type_.get_offset(b"name") + 4
    f = ctypes.CField(ctypes.c_int, 'name', -1)
    assert f.name == "name"
    assert f.offset == ctypes.c_int._type_.get_offset(b"name") - 4
    raises(TypeError, ctypes.CField, 1)
    raises(TypeError, ctypes.CField, ctypes.c_char)
    raises(TypeError, ctypes.CField, ctypes.c_char, 1)
    raises(TypeError, ctypes.CField, ctypes.
