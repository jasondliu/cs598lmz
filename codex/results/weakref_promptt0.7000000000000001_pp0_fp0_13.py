import weakref
# Test weakref.ref() and weakref.proxy()

from test import support

import weakref


class MyClass:
    pass

a = MyClass()

class TestRef:
    def test_basic(self):
        x = a
        weak = weakref.ref(x)
        self.assertIs(x, weak())
        del x
        self.assertIs(weak(), None)

    def test_call(self):
        # Check that ref objects behave like functions
        x = a
        weak = weakref.ref(x)
        self.assertIs(x, weak())
        del x
        self.assertIs(weak(), None)

    def test_hash(self):
        # Check that ref objects hash to the same value as the object they
        # reference
        x = a
        weak = weakref.ref(x)
        self.assertEqual(hash(x), hash(weak))
        ref2 = weakref.ref(x)
        self.assertEqual(hash(ref2), hash(weak))
        del x
        self.assertEqual(hash
