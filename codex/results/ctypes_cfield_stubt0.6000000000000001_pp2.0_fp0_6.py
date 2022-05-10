import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFieldTest(unittest.TestCase):

    # XXX: This is not a complete test suite.  It is only a
    # skeleton to show how to write a test and test the code
    # coverage.

    def test_basic(self):
        self.assertEqual(S.x.__class__, ctypes.CField)
        self.assertEqual(S.x.__name__, 'x')
        self.assertEqual(S.x._type_, ctypes.c_int)
        self.assertEqual(S.x.offset, 0)

    def test_get(self):
        s = S()
        self.assertEqual(S.x.get(s), 0)

    def test_set(self):
        s = S()
        S.x.set(s, 42)
        self.assertEqual(s.x, 42)

    def test_from_param(self):
        self.assertEqual(S.x.from_param(42), 42)

if __name__ == "__main
