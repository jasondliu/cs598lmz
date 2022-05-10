import ctypes
# Test ctypes.CField.from_address

class CFieldTest(unittest.TestCase):
    def test_from_address(self):
        class foo(ctypes.Structure):
            _fields_ = (("a", ctypes.c_char),
                        ("b", ctypes.c_int),
                        ("c", (ctypes.c_char * 4)))

        f = foo(65, 0x12345678, b"1234")
        self.assertEqual(ctypes.c_byte.from_address(ctypes.addressof(f)).value, f.a)

        try:
            field = ctypes.c_byte.from_address(bytes)
        except TypeError:
            pass # expected: bytes has no length attribute
        else:
            self.fail("exception expected here")

if __name__ == "__main__":
    unittest.main()
