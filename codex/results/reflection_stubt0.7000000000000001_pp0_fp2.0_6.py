fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class TestStr(unittest.TestCase):

    def test_set_immutable(self):
        self.assertRaises(TypeError, setattr, 'spam', '__code__', fn.__code__)
        self.assertRaises(TypeError, setattr, 'spam', '__dict__', {})
        self.assertRaises(TypeError, setattr, 'spam', '__class__', int)

    def test_translate(self):
        self.assertEqual('abcdefghijklmnop', ''.translate({ord('b'): None,
            ord('c'): None}))
        self.assertEqual('ad', ''.translate({ord('b'): None, ord('c'): 'd'}))
        self.assertEqual('ad', ''.translate({ord('b'): None, ord('c'): 'd',
            ord('a'): None}))
        self.assertEqual('ad', ''.translate({ord('b'): None, ord('c'): 'd
