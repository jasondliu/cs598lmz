import ctypes
# Test ctypes.CField
class FFF(ctypes.Structure):
    _fields_ = [
        ('first', ctypes.c_int),
        ('second', ctypes.c_short),
        ('third', ctypes.c_char * 8),
    ]
# Test a specific CField error
struct_field_type_error = raises(TypeError)(ctypes.CField)[
    None, None, None, None, None]

def test_field_structure():
    f = FFF()
    f.first = 1
    f.second = 2
    f.third = b"abcdefg"
    assert FFF.first.get(f) == 1
    assert FFF.second.get(f) == 2
    assert FFF.third.get(f) == b"abcdefg"
    FFF.first.set(f, 2)
    FFF.second.set(f, 3)
    FFF.third.set(f, b"ABCDEFG")
    assert f.first == 2
    assert f.second == 3
    assert f.third == b
