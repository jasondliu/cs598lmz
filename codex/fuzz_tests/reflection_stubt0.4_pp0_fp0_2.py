fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# 		self.assertRaises(TypeError, fn)

class CodeTest(unittest.TestCase):

    def test_code_attrs(self):
        def fn(a):
            b = 2
            return a + b
        self.assertEqual(fn.__code__.co_argcount, 1)
        self.assertEqual(fn.__code__.co_kwonlyargcount, 0)
        self.assertEqual(fn.__code__.co_nlocals, 2)
        self.assertEqual(fn.__code__.co_stacksize, 2)
        self.assertEqual(fn.__code__.co_flags, 67)
        self.assertEqual(fn.__code__.co_firstlineno, 1)
        self.assertEqual(fn.__code__.co_code, b'd\x01\x00Z\x00\x00d\x02\x00S\x00\x00')
        self.assertEqual(
