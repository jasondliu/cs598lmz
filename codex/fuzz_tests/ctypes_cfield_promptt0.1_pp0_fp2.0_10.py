import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long),
                        ("y", ctypes.c_long)]

        class RECT(ctypes.Structure):
            _fields_ = [("a", ctypes.c_long),
                        ("b", ctypes.c_long),
                        ("c", ctypes.c_long),
                        ("d", ctypes.c_long)]

        class MyUnion(ctypes.Union):
            _fields_ = [("pt", POINT),
                        ("rc", RECT)]

        class MyStruct(ctypes.Structure):
            _fields_ = [("a", ctypes.c_long),
                        ("b", ctypes.c_long),
                        ("un", MyUnion)]

        s = MyStruct()
        s.a = 1
        s.b = 2
        s.un.pt.x = 3
        s.un.pt.y = 4
       
