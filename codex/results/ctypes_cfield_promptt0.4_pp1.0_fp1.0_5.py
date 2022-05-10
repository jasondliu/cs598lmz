import ctypes
# Test ctypes.CField

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

    def __repr__(self):
        return "POINT(%d, %d)" % (self.x, self.y)

class RECT(ctypes.Structure):
    _fields_ = [("a", POINT),
                ("b", POINT)]
    def __repr__(self):
        return "RECT(%s, %s)" % (repr(self.a), repr(self.b))

class Test(unittest.TestCase):
    def test_field(self):
        r = RECT()
        self.assertEqual(r.a.x, 0)
        self.assertEqual(r.a.y, 0)
        self.assertEqual(r.b.x, 0)
        self.assertEqual(r.b.y, 0)

        r.a.x = 1
        r.a.y = 2
       
