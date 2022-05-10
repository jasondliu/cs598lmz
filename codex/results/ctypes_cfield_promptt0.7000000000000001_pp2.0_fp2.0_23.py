import ctypes
# Test ctypes.CField
#

class FieldTestCase(unittest.TestCase):

    def test_fields(self):
        import _ctypes_test
        dll = ctypes.CDLL(_ctypes_test.__file__)
        b = ctypes.c_byte(16)
        self.failUnless(b.value == 16)
        b.value = 42
        self.failUnless(b.value == 42)
        b.value = ctypes.c_byte(-1)
        self.failUnless(b.value == -1)

        s = ctypes.c_short(16)
        self.failUnless(s.value == 16)
        s.value = 42
        self.failUnless(s.value == 42)
        s.value = ctypes.c_short(-1)
        self.failUnless(s.value == -1)

        i = ctypes.c_int(16)
        self.failUnless(i.value == 16)
        i.value = 42
        self.failUnless(i.value == 42)
        i.value = c
