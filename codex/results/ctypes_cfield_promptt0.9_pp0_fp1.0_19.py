import ctypes
# Test ctypes.CField
# http://docs.python.org/3.3/library/ctypes.html#ctypes.CField

class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class AnyStruct(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int)]
        f = ctypes.CField(AnyStruct, 'a',
                          ctypes.c_double, 0,
                          ctypes.sizeof(AnyStruct), AnyStruct)
        self.assertEqual(f.name, 'a')
        self.assertEqual(f._fieldtype_, ctypes.c_double)
        self.assertEqual(f.offset, 0)
        self.assertEqual(f.size, 4)
        self.assertEqual(f._ctype_)

    def test_subclass(self):
        class Struct(ctypes.Structure):
            _fields_ = [('sub', 'b')]

        class Struct2(Struct):
            _fields_ = [('a', ctypes.c
