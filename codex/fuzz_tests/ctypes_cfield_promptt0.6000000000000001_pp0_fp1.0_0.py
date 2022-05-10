import ctypes
# Test ctypes.CField.from_address

import ctypes.test.test_cfield

class Test(ctypes.test.test_cfield.Test):
    def test_from_address(self):
        import ctypes.wintypes
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long),
                        ("y", ctypes.c_long)]

        # address of POINT.x
        addr = ctypes.addressof(POINT().x)
        # the field is a pointer to a c_long, this is a value
        self.assertTrue(isinstance(addr, ctypes.wintypes._LONG_PTR))
        # the POINT.x field
        field = ctypes.CField.from_address(addr)
        self.assertEqual(field.name, "x")
        # the POINT structure
        struc = field.structure
        self.assertEqual(struc.__name__, "POINT")
        # the POINT type
        cls = struc.__class__

