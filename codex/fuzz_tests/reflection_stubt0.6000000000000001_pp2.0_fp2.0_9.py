fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


class TestCode(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(fn.__code__), "<code object <lambda> at 0x%x, file '%s', line %d>" % (
            id(fn.__code__), __file__, fn.__code__.co_firstlineno))

    def test_attributes(self):
        self.assertEqual(fn.__code__.co_argcount, 0)
        self.assertEqual(fn.__code__.co_filename, __file__)
        self.assertEqual(fn.__code__.co_firstlineno, fn.__code__.co_lnotab)
        self.assertEqual(fn.__code__.co_flags, 0)
        self.assertEqual(fn.__code__.co_name, '<lambda>')
        self.assertEqual(fn.__code__.co_names, ())
        self.assertEqual(fn.__code__
