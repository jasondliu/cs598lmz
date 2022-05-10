import ctypes
# Test ctypes.CField
class TestCField:
    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [
                ('a', ctypes.c_int),
                ('b', ctypes.CField)]
        x = X()
        # The treatment of empty fields is platform specific
        assert x.b is 0 or x.b is None

    def test_struct(self):
        class Z(ctypes.Structure):
            _fields_ = [('a', ctypes.c_char)]
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int),
                        ('b', Z)]
        x = X()
        x.b.a = '?'
        assert x.b.a == '?'

    def test_create(self):
        class Z(ctypes.Structure):
            _fields_ = [('a', ctypes.c_char)]
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int),
                        ('b',
