import types
types.MethodType(lambda self: None, None, Dummy)

# do not complain about *, **
# pylint: disable=W0142

class Test_Dummy(unittest.TestCase):
    def test_constructor(self):
        x = Dummy()
        self.assertEqual(x.foo, 'foo')
        x.foo = 'bar'
        self.assertEqual(x.foo, 'bar')
        x.bar = 'foo'
        self.assertEqual(x.bar, 'foo')

    def test_len(self):
        x = Dummy()
        self.assertEqual(len(x), 2)
        x.bar = 'foo'
        self.assertEqual(len(x), 3)

    def test_contains(self):
        x = Dummy()
        self.assertTrue('foo' in x)
        self.assertFalse('bar' in x)
        x.bar = 'foo'
        self.assertTrue('bar' in x)

    def test_iter(self):
       
