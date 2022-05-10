import ctypes
# Test ctypes.CField.from_address(p_instance, addr)

class C(ctypes.Structure):
    _fields_ = [("stuff", ctypes.c_int),
                ("more_stuff", ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [("stuff", ctypes.c_int),
                ("b", C)]

class A(ctypes.Structure):
    _fields_ = [("stuff", ctypes.c_int),
                ("b1", B),
                ("b2", B)]

class Test(unittest.TestCase):
    def test_cfield_from_address(self):
        a = A()
        self.assertEqual(ctypes.c_int.from_address(a, ctypes.addressof(a.stuff)),
                                 ctypes.c_int(0))
        self.assertEqual(ctypes.c_int.from_address(a, ctypes.addressof(a.b1.stuff)),
                                 ctypes.c_int(0))

