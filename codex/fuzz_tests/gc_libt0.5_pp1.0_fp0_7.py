import gc, weakref

#------------------------------------------------------------------------------

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return isinstance(other, Foo) and self.name == other.name

class Bar(object):
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return isinstance(other, Bar) and self.name == other.name

#------------------------------------------------------------------------------

class TestWeakKeyDictionary(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, weakref.WeakKeyDictionary, None)
        self.assertRaises(TypeError, weakref.WeakKeyDictionary, 42)
        self.assertRaises(TypeError, weakref.WeakKeyDictionary, 3.14)
        self.assertRaises(TypeError, weakref.WeakKeyDictionary, "foo")
        self.assertRaises(TypeError, weakref.WeakKeyDictionary, [])
        self
