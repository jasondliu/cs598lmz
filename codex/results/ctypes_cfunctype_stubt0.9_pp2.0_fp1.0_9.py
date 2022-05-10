import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object(None)

class Test(unittest.TestCase):

    def test_type(self):
        self.assertIs(type(void_p), type(FUNTYPE))

    def test_equal(self):
        self.assertEqual(void_p, FUNTYPE)

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, 'modes are not coercible.+'):
            not void_p
        with self.assertRaisesRegex(TypeError, 'modes are not coercible.+'):
            if void_p: pass
        with self.assertRaisesRegex(TypeError, 'modes are not coercible.+'):
            for void_p: pass

    def test_equal_other_type(self):
        self.assertTrue(void_p != FUNTYPE)
        for cls in type, int, str, list, fun:
            self.assertIs(void_p == cls, NotImplemented)
            self.assertIs(cls == void_p
