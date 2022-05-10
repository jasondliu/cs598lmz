import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert isinstance(S.x, ctypes.Field)
    assert isinstance(S.x, ctypes.MemberDescriptorType)
    assert S.x.__objclass__ is S
    assert S.x.__name__ == 'x'
    assert S.x.__doc__ == 'x(self) -> int\n\n'
    assert S.x.offset == 0
    assert S.x.size == 4
    assert S.x.index == 0
    assert S.x.pack == 1
    assert S.x.ctype is ctypes.c_int
    assert S.x.type is int
    assert S.x.bits == 32
    assert S.x.flags == 0
    assert S.x.num_bytes == 4
    assert S.x.num_elements == 1
    assert S.x.num_from_string_elements == 1
    assert S.x.from_param is ctypes.c_int.from
