import ctypes
# Test ctypes.CField.from_param

class TestFromParam:
    class C(ctypes.Structure):
        _fields_ = [
            ("x", ctypes.c_int),
            ("y", ctypes.c_int),
        ]

    def test_basic(self):
        c = self.C()
        c.x = 1
        c.y = 2
        assert c.x == 1
        assert c.y == 2
        assert self.C.x.from_param(c) == 1
        assert self.C.y.from_param(c) == 2

    def test_subclass(self):
        class C(self.C):
            pass
        c = C()
        c.x = 1
        c.y = 2
        assert c.x == 1
        assert c.y == 2
        assert self.C.x.from_param(c) == 1
        assert self.C.y.from_param(c) == 2

    def test_subclass_override(self):
        class C(self.C):
            _fields_
