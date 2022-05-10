import ctypes
# Test ctypes.CField

def test_field_bitfields(self):

    assert not ctypes.sizeof(ctypes.c_longdouble) in (8, 12, 16)

    for k in range(2, 17, 2):
        class X(ctypes.Structure):
            a = ctypes.c_longdouble
            _pack_ = 1
            _fields_ = [('x', ctypes.c_byte, k), ('y', ctypes.c_byte, 16 - k)]

        assert ctypes.sizeof(X) == 2
        assert ctypes.alignment(X) == 1

        obj = X()
        obj.x = -1
        obj.y = -1
        assert hex(ctypes.c_long(ctypes.addressof(obj))) == hex(ctypes.c_long(ctypes.addressof(obj.x)))

        obj = X()
        obj.x = -1
        obj.y = -1
        value = ((ctypes.c_ushort(obj.y).value << k) | ctypes.c_ushort(obj
