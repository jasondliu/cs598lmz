import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert ctypes.CField is ctypes.c_int

class Union(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(Union.x)
assert ctypes.CUnion is ctypes.c_int

class TestEnum(unittest.TestCase):
    def test_enum(self):
        class E(ctypes.c_int):
            _fields_ = [("A", ctypes.c_int), ("B", ctypes.c_int)]
        assert E.A == 0
        assert E.B == 1

        self.assertRaises(TypeError, E, 0)
        self.assertRaises(TypeError, E, 0, 1)

        self.assertRaises(ValueError, setattr, E, "A", 1)

        assert E(E.A) == 0
        assert E(E.B) == 1

        self.assertRaises(TypeError, E, "A")
        self.assertRaises(ValueError, E, "C")


