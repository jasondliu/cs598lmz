import ctypes
# Test ctypes.CField
class TestCStruct(object):
    def setup_method(self, meth):
        class C(ctypes.Structure):
            _fields_ = [('foo', ctypes.c_int),
                        ('bar', ctypes.c_int),
                        ('baz', ctypes.c_double),
                        ]
        self.C = C
        # For testing.  Its type must be known to the compiler, so we
        # don't use ctypes.c_void_p.
        self.void_p = ctypes.c_char_p()
        flags = [('bar', ctypes.c_int, 2),
                 ('foo', ctypes.c_int, 14),
                 ]
        self.C2 = ctypes.create_struct_type(flags)
        self.C2._anonymous_ = [('bar', ctypes.c_int)]
    def test_not_contigous(self):
        C3 = self.C2 * 3
        raises(TypeError, ctypes.c_byte, C3)
    def test_offsetof(self
