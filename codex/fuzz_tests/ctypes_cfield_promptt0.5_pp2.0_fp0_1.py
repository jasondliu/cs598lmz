import ctypes
# Test ctypes.CField.from_address()

class MyStructure(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class MyUnion(ctypes.Union):
    _fields_ = [("b", ctypes.c_int)]

class MyStructureWithUnion(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("myunion", MyUnion)]

class MyStructureWithPointer(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("p", ctypes.POINTER(ctypes.c_int))]

class Test(unittest.TestCase):
    def test_structure_from_address(self):
        s = MyStructure()
        p = ctypes.pointer(s)
        f = ctypes.CField.from_address(p, MyStructure)
        self.assertEqual(f.offset, 0)
        self.assertEqual(f.size, ctypes.sizeof(ctypes.
