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
