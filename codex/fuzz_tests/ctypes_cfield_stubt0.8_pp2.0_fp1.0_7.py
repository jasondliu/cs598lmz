import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class IntrospectionTestCase(unittest.TestCase):
    def test_fields(self):
        S._fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]
        self.assertEqual(S._fields_, [('a', ctypes.c_int),
                                      ('b', ctypes.c_int)])

    def test_addressof(self):
        # XXX addressof(string) currently fails because strings are
        # copied into an array of characters.
        s = ctypes.c_int(42)
        self.assertTrue(ctypes.addressof(s))

    def test_sizeof(self):
        self.assertEqual(ctypes.sizeof(ctypes.c_int), ctypes.sizeof(ctypes.c_long))
        if ctypes.sizeof(ctypes.c_long) > 4:
            self.assertEqual(ctypes.sizeof(ctypes.c_int), 4)

    def test_alignment(self):
        self
