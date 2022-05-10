import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test___init__(self):
        self.assertRaises(AttributeError, ctypes.CField,
                          ctypes.c_int, 'a', 'b')

    def test___repr__(self):
        self.assertEqual(repr(ctypes.CField(ctypes.c_int, 'a')),
                         "<CField type 'int' of 'CFieldTest' at %x>" %
                         id(ctypes.CField(ctypes.c_int, 'a')))

    def test_from_address(self):
        class S(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int)]

        s = S()
        a = ctypes.c_int.from_address(ctypes.addressof(s) + ctypes.sizeof(ctypes.c_int))
        self.assertEqual(a.value, 0)
        a.value = 42
        self.assertEqual(s.a, 42)

   
