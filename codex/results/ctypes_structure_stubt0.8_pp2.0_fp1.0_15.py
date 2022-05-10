import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(2)
    y = ctypes.c_double(3)
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

class Point3D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

class Test(unittest.TestCase):
    def test_nested_struct(self):
        class Nested(ctypes.Structure):
            _fields_ = ("s", S)

        n = Nested(S())
        self.assertEqual(n.s, S())
        # Test that the internal reference works
        n.s = S()
        self.assertEqual(n.s, S())
        n2 =
